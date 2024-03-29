# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from middleware.protoBuffers import movel_pb2 as movel__pb2


class MovelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.criarMovel = channel.unary_unary(
                '/Movel/criarMovel',
                request_serializer=movel__pb2.CriarMovel.SerializeToString,
                response_deserializer=movel__pb2.RespostaCriarMovel.FromString,
                )
        self.excluirMovel = channel.unary_unary(
                '/Movel/excluirMovel',
                request_serializer=movel__pb2.ExcluirMovel.SerializeToString,
                response_deserializer=movel__pb2.RespostaExcluirMovel.FromString,
                )
        self.buscarMoveis = channel.unary_unary(
                '/Movel/buscarMoveis',
                request_serializer=movel__pb2.BuscarMoveis.SerializeToString,
                response_deserializer=movel__pb2.RespostaBuscarMoveis.FromString,
                )


class MovelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def criarMovel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def excluirMovel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buscarMoveis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MovelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'criarMovel': grpc.unary_unary_rpc_method_handler(
                    servicer.criarMovel,
                    request_deserializer=movel__pb2.CriarMovel.FromString,
                    response_serializer=movel__pb2.RespostaCriarMovel.SerializeToString,
            ),
            'excluirMovel': grpc.unary_unary_rpc_method_handler(
                    servicer.excluirMovel,
                    request_deserializer=movel__pb2.ExcluirMovel.FromString,
                    response_serializer=movel__pb2.RespostaExcluirMovel.SerializeToString,
            ),
            'buscarMoveis': grpc.unary_unary_rpc_method_handler(
                    servicer.buscarMoveis,
                    request_deserializer=movel__pb2.BuscarMoveis.FromString,
                    response_serializer=movel__pb2.RespostaBuscarMoveis.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Movel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Movel(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def criarMovel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Movel/criarMovel',
            movel__pb2.CriarMovel.SerializeToString,
            movel__pb2.RespostaCriarMovel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def excluirMovel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Movel/excluirMovel',
            movel__pb2.ExcluirMovel.SerializeToString,
            movel__pb2.RespostaExcluirMovel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buscarMoveis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Movel/buscarMoveis',
            movel__pb2.BuscarMoveis.SerializeToString,
            movel__pb2.RespostaBuscarMoveis.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
