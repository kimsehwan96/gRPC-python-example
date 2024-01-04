# envoy-example

`$ docker run -p 9901:9901 -p 10000:10000 -v ../proto/helloworld.pb:/etc/envoy/helloworld.pb -v ../envoy.yaml:/etc/envoy/envoy.yaml --add-host host.docker.internal:host-gateway envoyproxy/envoy:dev-2f8e1a36ed808d760d6f791cdfc8f8cd568a1ad7`

`$ curl -XGET localhost:7777/v1/hello`
