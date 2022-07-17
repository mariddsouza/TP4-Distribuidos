import grpc
from concurrent import futures
import time
from middleware.protoBuffers import usuario_pb2_grpc,movel_pb2_grpc,proposta_pb2_grpc
from middleware.servidor_midd import ServidorMidd
from models.usuario import Usuario
from middleware.servidor_midd import *


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


usuario_pb2_grpc.add_UsuarioServicer_to_server(
        UsuarioServicer(), server)
movel_pb2_grpc.add_MovelServicer_to_server(
        MovelServicer(), server)
proposta_pb2_grpc.add_propostaServicer_to_server(
    PropostaServicer(),server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('localhost:55501')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)