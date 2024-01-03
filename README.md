# gRPC-python-example

gRPC 테스트

## Install

## Server Reflection

`python3 -m pip install grpcio-reflection`

## proto to python files

example.

`$ python3 -m grpc_tools.protoc -I ./proto --python_out=./test --pyi_out=./test --grpc_python_out=./test ./proto/helloworld.proto`

## proto build

`$ protoc -I ./googleapis -I ./proto --include_imports --include_source_info --descriptor_set_ou
t=proto/helloworld.pb proto/helloworld.proto`

## grpcurl

macos
`$ brew install grpcurl`

`$ grpcurl -plaintext localhost:50051 list helloworld.Greeter`

```
~ ❯ grpcurl -plaintext localhost:50051 list helloworld.Greeter
helloworld.Greeter.SayHello
```

`$ grpcurl -plaintext localhost:50051 helloworld.Greeter.SayHello`

```
~ ❯ grpcurl -plaintext -d '{"name": "hayden"}' localhost:50051 helloworld.Greeter.SayHello
{
  "message": "Hello, hayden!"
}
```

## DIY

1. proto 파일 수정

2. server 코드 수정 (해당 메서드 호출시 어떤 응답을 할지)

3. `python3 -m grpc_tools.protoc -I ./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/helloworld.proto` 로 업데이트

4. 실행

`$ grpcurl -plaintext localhost:50051 list helloworld.Greeter`

## Health Check

`grpc.health.v1.Health` 형태로 사전에 정의된 프로토버퍼 형태도 있고 응답도 있음.

`python3 -m pip install grpcio-health-checking`

`$ grpcurl -plaintext localhost:50051 grpc.health.v1.Health/Check`
`$ grpcurl -plaintext localhost:50051 grpc.health.v1.Health/Watch`

-> K8s 의 gRPC Health Check 는 이 엔드포인트를 바라보는건지 확인 필요함


```
~ ❯ grpcurl -plaintext localhost:50051 grpc.health.v1.Health/Check
{
  "status": "SERVING"
}
```

## TODO

Add makefile for protobuf into python code automation
Add more examples
