# Copyright 2018 The gRPC Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The reflection-enabled version of gRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import threading
from time import sleep
import os
import grpc
from grpc_reflection.v1alpha import reflection
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
import helloworld_pb2
import helloworld_pb2_grpc


SERVER_PORT = os.environ.get("SERVER_PORT", 7777)

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)
    
    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello again, %s!" % request.name)


def _toggle_health(health_servicer: health.HealthServicer, service: str):
    # Health Check 요청 들어왔을 때, 서비스 상태를 번갈아가면서 응답
    next_status = health_pb2.HealthCheckResponse.SERVING
    while True:
        if next_status == health_pb2.HealthCheckResponse.SERVING:
            next_status = health_pb2.HealthCheckResponse.NOT_SERVING
        else:
            next_status = health_pb2.HealthCheckResponse.SERVING
        
        health_servicer.set(service, next_status)
        sleep(5)
        print(f"Set {service} to {next_status}")

def _configure_heath_server(server: grpc.Server):
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=10),
    )
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    
    toggle_health_status_thread = threading.Thread(
        target=_toggle_health, args=(health_servicer, "helloworld.Greeter"),
        daemon=True
    )
    toggle_health_status_thread.start()
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    SERVICE_NAMES = (
        helloworld_pb2.DESCRIPTOR.services_by_name["Greeter"].full_name,
        reflection.SERVICE_NAME,
        health.SERVICE_NAME,
    )
    server.add_insecure_port(f"[::]:{SERVER_PORT}")
    _configure_heath_server(server)
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

# This server has server reflection enabled, which means that it can be queried
