# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..grpc_author import author_pb2 as author__pb2


class GrpcAuthorsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAuthor = channel.unary_unary(
            '/GrpcAuthors/GetAuthor',
            request_serializer=author__pb2.GetAuthorRequest.SerializeToString,
            response_deserializer=author__pb2.AuthorGrpc.FromString,
        )


class GrpcAuthorsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAuthor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcAuthorsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAuthor': grpc.unary_unary_rpc_method_handler(
            servicer.GetAuthor,
            request_deserializer=author__pb2.GetAuthorRequest.FromString,
            response_serializer=author__pb2.AuthorGrpc.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'GrpcAuthors', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class GrpcAuthors(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAuthor(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcAuthors/GetAuthor',
                                             author__pb2.GetAuthorRequest.SerializeToString,
                                             author__pb2.AuthorGrpc.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)