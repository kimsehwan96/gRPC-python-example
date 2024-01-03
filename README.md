# gRPC-python-example

gRPC 테스트

## Install

## Server Reflection

`python3 -m pip install grpcio-reflection`

## proto to python files

example.

`$ python3 -m grpc_tools.protoc -I ./proto --python_out=./test --pyi_out=./test --grpc_python_out=./test ./proto/helloworld.proto`

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
~ ❯ grpcurl -plaintext localhost:50051 helloworld.Greeter.SayHello
{
  "message": "Hello, !"
}
```

