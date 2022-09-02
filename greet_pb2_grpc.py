# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greet_pb2 as greet__pb2


class GreeterStub(object):
    """The greeting service definition.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/greet.Greeter/SayHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )
        self.ParrotSaysHello = channel.unary_stream(
                '/greet.Greeter/ParrotSaysHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )
        self.ChattyClientSaysHello = channel.stream_unary(
                '/greet.Greeter/ChattyClientSaysHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.DelayedReply.FromString,
                )
        self.InteractingHello = channel.stream_stream(
                '/greet.Greeter/InteractingHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.

    """

    def SayHello(self, request, context):
        """unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ParrotSaysHello(self, request, context):
        """Server Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChattyClientSaysHello(self, request_iterator, context):
        """Client Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InteractingHello(self, request_iterator, context):
        """Both Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
            'ParrotSaysHello': grpc.unary_stream_rpc_method_handler(
                    servicer.ParrotSaysHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
            'ChattyClientSaysHello': grpc.stream_unary_rpc_method_handler(
                    servicer.ChattyClientSaysHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.DelayedReply.SerializeToString,
            ),
            'InteractingHello': grpc.stream_stream_rpc_method_handler(
                    servicer.InteractingHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.

    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/SayHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ParrotSaysHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greet.Greeter/ParrotSaysHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChattyClientSaysHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/greet.Greeter/ChattyClientSaysHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.DelayedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InteractingHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/greet.Greeter/InteractingHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
