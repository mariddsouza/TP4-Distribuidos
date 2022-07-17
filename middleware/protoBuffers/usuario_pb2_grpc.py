# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from middleware.protoBuffers import usuario_pb2 as usuario__pb2


class UsuarioStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/Usuario/login',
                request_serializer=usuario__pb2.BuscarUsuario.SerializeToString,
                response_deserializer=usuario__pb2.User.FromString,
                )
        self.getTodosUsuarios = channel.unary_unary(
                '/Usuario/getTodosUsuarios',
                request_serializer=usuario__pb2.BuscarTodosUsuarios.SerializeToString,
                response_deserializer=usuario__pb2.RespostaBuscarTodosUsuarios.FromString,
                )
        self.cadastrarUsuario = channel.unary_unary(
                '/Usuario/cadastrarUsuario',
                request_serializer=usuario__pb2.User.SerializeToString,
                response_deserializer=usuario__pb2.RespostaCadastrarUsuario.FromString,
                )


class UsuarioServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTodosUsuarios(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cadastrarUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsuarioServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=usuario__pb2.BuscarUsuario.FromString,
                    response_serializer=usuario__pb2.User.SerializeToString,
            ),
            'getTodosUsuarios': grpc.unary_unary_rpc_method_handler(
                    servicer.getTodosUsuarios,
                    request_deserializer=usuario__pb2.BuscarTodosUsuarios.FromString,
                    response_serializer=usuario__pb2.RespostaBuscarTodosUsuarios.SerializeToString,
            ),
            'cadastrarUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.cadastrarUsuario,
                    request_deserializer=usuario__pb2.User.FromString,
                    response_serializer=usuario__pb2.RespostaCadastrarUsuario.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Usuario', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Usuario(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Usuario/login',
            usuario__pb2.BuscarUsuario.SerializeToString,
            usuario__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTodosUsuarios(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Usuario/getTodosUsuarios',
            usuario__pb2.BuscarTodosUsuarios.SerializeToString,
            usuario__pb2.RespostaBuscarTodosUsuarios.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cadastrarUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Usuario/cadastrarUsuario',
            usuario__pb2.User.SerializeToString,
            usuario__pb2.RespostaCadastrarUsuario.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
