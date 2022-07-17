import json
import re
import socket
from typing import List
from cliente.cadastro import Cadastro
from models.movel import Movel
from models.proposta import Proposta
from models.tipo_operacao import TipoOperacao
from middleware.protoBuffers import usuario_pb2,usuario_pb2_grpc,movel_pb2,movel_pb2_grpc,proposta_pb2_grpc,proposta_pb2
from models.usuario import Usuario
from banco.cadastro import aceitaProposta, buscarMoveis, deletarMovel, inserirUsuario, inserirMovel
from banco.cadastro import buscarUsuarioBanco
from banco.cadastro import atualizaBanco
from banco.cadastro import listarUsuarios
from banco.cadastro import criarProposta
from banco.cadastro import buscaMovel
from banco.cadastro import buscaPropostaRealizada
from banco.cadastro import buscaPropostaRecebida
from banco.cadastro import recusaProposta

class ServidorMidd:
    def __init__(self) -> None:
        pass
    
class UsuarioServicer(usuario_pb2_grpc.UsuarioServicer):
    def login(self, request, context):
        response = usuario_pb2.User()
        usuario:Usuario = buscarUsuarioBanco(cpf=request.cpf,senha=request.senha)
        response.nome = usuario.nome
        response.cpf = usuario.cpf
        response.senha =usuario.senha
        return response

    def getTodosUsuarios(self, request, context):
        usuarios = listarUsuarios()
        response= usuario_pb2.RespostaBuscarTodosUsuarios()
        for usuario in usuarios:
            users=response.usuario.add()
            users.nome = usuario.nome
            users.cpf = usuario.cpf
            users.senha = usuario.senha                    
        return response
    
    def cadastrarUsuario(self, request, context):
        usuario:Usuario =Usuario(nome=request.nome,cpf=request.cpf,senha=request.senha)
        response = usuario_pb2.RespostaCadastrarUsuario()
        response.status=inserirUsuario(usuario)
        return  response
       

class MovelServicer(movel_pb2_grpc.MovelServicer):
    def criarMovel(self, request, context):
        furniture = request.movel
        movel:Movel =Movel(nome=furniture.nome,tempoUso=furniture.tempoUso,descricao=furniture.descricao)
        response = movel_pb2.RespostaCriarMovel()
        response.status=inserirMovel(request.cpf, movel)
        return  response
    def excluirMovel(self, request, context):
        response = movel_pb2.RespostaExcluirMovel()
        response.status= deletarMovel(idMovel=request.idMovel,cpf=request.cpf)
        return response
    def buscarMoveis(self, request, context):
        try:
            moveis = buscarMoveis(cpf=request.cpf)
            response= movel_pb2.RespostaBuscarMoveis()
            for movel in moveis:
                furniture=response.moveis.add()
                furniture.nome = movel.nome
                furniture.tempoUso = int(movel.tempoUso)
                furniture.descricao = movel.descricao
                furniture.id = movel.id
            return response
        except Exception as e:
            print(e)
            return None

class PropostaServicer(proposta_pb2_grpc.propostaServicer):
    def fazerProposta(self, request, context):
        try:
            response = proposta_pb2.RespostaFazerProposta()
            response.status=criarProposta(request.idMovelRequerido, request.idMovelProposto,
            request.cpfUsuarioRequisitante, request.cpfUsuarioRequisitado)
            return  response
        except Exception as e:
            print(e)
    
    def buscarPropostasRealizadas(self, request, context):
        propostas =  buscaPropostaRealizada(request.cpf)
        response= proposta_pb2.RespostaBuscarPropostasRealizadas()
       

        for proposta in propostas:
            propostas=response.propostas.add()
            propostas.idProposta = int(proposta.idProposta)
           
            propostas.usuarioAlvo.nome = proposta.usuarioAlvo.nome
            propostas.usuarioAlvo.senha = proposta.usuarioAlvo.senha
            propostas.usuarioAlvo.cpf = proposta.usuarioAlvo.cpf

            propostas.usuarioRequisitante.nome = proposta.usuarioRequisitante.nome
            propostas.usuarioRequisitante.senha = proposta.usuarioRequisitante.senha
            propostas.usuarioRequisitante.cpf = proposta.usuarioRequisitante.cpf
           
            propostas.movelProposto.id=proposta.movelProposto.id
            propostas.movelProposto.descricao=proposta.movelProposto.descricao
            propostas.movelProposto.tempoUso=int(proposta.movelProposto.tempoUso)
            propostas.movelProposto.nome= proposta.movelProposto.nome
            
            propostas.movelRequerido.id=proposta.movelRequerido.id
            propostas.movelRequerido.descricao=proposta.movelRequerido.descricao
            propostas.movelRequerido.tempoUso=int(proposta.movelRequerido.tempoUso)
            propostas.movelRequerido.nome= proposta.movelRequerido.nome
            propostas.status = proposta.status
        return response

    def aceitarProposta(self, request, context):
        status = aceitaProposta(request.id,cpfUsuarioAlvo=request.cpfUsuarioAlvo)
        response = proposta_pb2.StatusResposta(status=status)
        return response
    
    def recusarProposta(self, request, context):
        status = recusaProposta(request.id,cpfUsuarioAlvo=request.cpfUsuarioAlvo)
        response = proposta_pb2.StatusResposta(status=status)
        return response
    
    def buscarPropostasRecebidas(self, request, context):
        propostas =   buscaPropostaRecebida(request.cpf)
        response= proposta_pb2.RespostaBuscarPropostasRealizadas()
       

        for proposta in propostas:
            propostas=response.propostas.add()
            propostas.idProposta = int(proposta.idProposta)
           
            propostas.usuarioAlvo.nome = proposta.usuarioAlvo.nome
            propostas.usuarioAlvo.senha = proposta.usuarioAlvo.senha
            propostas.usuarioAlvo.cpf = proposta.usuarioAlvo.cpf

            propostas.usuarioRequisitante.nome = proposta.usuarioRequisitante.nome
            propostas.usuarioRequisitante.senha = proposta.usuarioRequisitante.senha
            propostas.usuarioRequisitante.cpf = proposta.usuarioRequisitante.cpf
           
            propostas.movelProposto.id=proposta.movelProposto.id
            propostas.movelProposto.descricao=proposta.movelProposto.descricao
            propostas.movelProposto.tempoUso=int(proposta.movelProposto.tempoUso)
            propostas.movelProposto.nome= proposta.movelProposto.nome
            
            propostas.movelRequerido.id=proposta.movelRequerido.id
            propostas.movelRequerido.descricao=proposta.movelRequerido.descricao
            propostas.movelRequerido.tempoUso=int(proposta.movelRequerido.tempoUso)
            propostas.movelRequerido.nome= proposta.movelRequerido.nome
            propostas.status = proposta.status
        return response

    
        
        
