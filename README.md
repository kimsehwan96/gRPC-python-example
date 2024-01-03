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
