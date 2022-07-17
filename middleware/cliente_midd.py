import json
import socket
from typing import List

import grpc
from models.movel import Movel
from models.proposta import Proposta
from models.status_resposta import StatusResposta
from  models.tipo_operacao import TipoOperacao
from middleware.protoBuffers import usuario_pb2_grpc,usuario_pb2,movel_pb2,movel_pb2_grpc,proposta_pb2,proposta_pb2_grpc
from models.usuario import Usuario

class ClienteMidd:
    def __init__(self) -> None:
      self.channel = grpc.insecure_channel('localhost:55501')
       
    def criarUsuario(self,usuario:Usuario)-> int:
      try:
            stub = usuario_pb2_grpc.UsuarioStub(self.channel)
            usuario = usuario_pb2.User(nome=usuario.nome,cpf=usuario.cpf,senha=usuario.senha)
            response = stub.cadastrarUsuario(usuario)
            return response.status
      except Exception as e:
         print(e)
         return None
       
    
    def buscarUsuario(self,cpf:int,senha:str)-> Usuario:
         try:
            stub = usuario_pb2_grpc.UsuarioStub(self.channel)
            usuario = usuario_pb2.BuscarUsuario(cpf=cpf,senha=senha)
            response = stub.login(usuario)
            return Usuario(nome=response.nome,cpf=response.cpf,senha=response.senha,
                  moveis=[],propostasFeitas=[],propostasRecebidas=[])
         except Exception as e:
               print(e)
               return None

    def buscarMoveis(self,cpf:int)->List[Movel]:
      try:
            stub = movel_pb2_grpc.MovelStub(self.channel)
            buscarMoveis = movel_pb2.BuscarMoveis(cpf=cpf)
            response = stub.buscarMoveis(buscarMoveis)
            moveis = []
            for movel in response.moveis:
               moveis.append(Movel(nome=movel.nome,tempoUso=movel.tempoUso,id=movel.id,
               descricao=movel.descricao))
            return moveis
      except Exception as e :
         print(e)
         return None
       
    
    def buscarTodosUsuarios(self)-> list:
       try:
            stub = usuario_pb2_grpc.UsuarioStub(self.channel)
            usuario = usuario_pb2.BuscarTodosUsuarios()
            response = stub.getTodosUsuarios(usuario)
            usuarios = []
            for usuario in response.usuario:
               usuarios.append(Usuario(nome=usuario.nome,cpf=usuario.cpf,senha=usuario.senha,
                  moveis=[],propostasFeitas=[],propostasRecebidas=[]))
            return usuarios
       except Exception as e :
         print(e)
         return None
      

    def buscarPropostasRealizadas(self,cpf:int)->List[Proposta]:
      try:
            stub = proposta_pb2_grpc.propostaStub(self.channel)
            request = proposta_pb2.BuscarPropostasRealizadas()
            request.cpf = cpf
            response = stub.buscarPropostasRealizadas(request)
            propostas = []
             
            for proposta in response.propostas:
               userAlvo = proposta.usuarioAlvo
               userRequisitante = proposta.usuarioRequisitante
               furnitureProposto = proposta.movelProposto
               furnitureRequerido = proposta.movelRequerido
               usuarioAlvo = Usuario(nome=userAlvo.nome,cpf=userAlvo.cpf,senha=userAlvo.senha,
                  moveis=[],propostasFeitas=[],propostasRecebidas=[])
               usuarioRequisitante = Usuario(nome=userRequisitante.nome,cpf=userRequisitante.cpf,senha=userRequisitante.senha,
                  moveis=[],propostasFeitas=[],propostasRecebidas=[])
               movelProposto =Movel(nome=furnitureProposto.nome,tempoUso=furnitureProposto.tempoUso,id=furnitureProposto.id,
               descricao=furnitureProposto.descricao)
               movelRequerido =Movel(nome=furnitureRequerido.nome,tempoUso=furnitureRequerido.tempoUso,id=furnitureRequerido.id,
               descricao=furnitureRequerido.descricao)
               propostas.append(Proposta(idProposta=proposta.idProposta,usuarioAlvo=usuarioAlvo,usuarioRequisitante=usuarioRequisitante
               ,movelProposto=movelProposto,movelRequerido=movelRequerido,status=proposta.status))
            return propostas
      except Exception as e :
         print(e,"saa")
         return None
    
    def buscarPropostasRecebidas(self,cpf:int)->List[Proposta]:
      try:
            stub = proposta_pb2_grpc.propostaStub(self.channel)
            request = proposta_pb2.BuscarPropostasRecebidas()
            request.cpf = cpf
            response = stub.buscarPropostasRecebidas(request)
            propostas = []
             
            for proposta in response.propostas:
               userAlvo = proposta.usuarioAlvo
               userRequisitante = proposta.usuarioRequisitante
               furnitureProposto = proposta.movelProposto
               furnitureRequerido = proposta.movelRequerido
               usuarioAlvo = Usuario(nome=userAlvo.nome,cpf=userAlvo.cpf,senha=userAlvo.senha,
                  moveis=[],propostasFeitas=[],propostasRecebidas=[])
               usuarioRequisitante = Usuario(nome=userRequisitante.nome,cpf=userRequisitante.cpf,senha=userRequisitante.senha,
                  moveis=[],propostasFeitas=[],propostasRecebidas=[])
               movelProposto =Movel(nome=furnitureProposto.nome,tempoUso=furnitureProposto.tempoUso,id=furnitureProposto.id,
               descricao=furnitureProposto.descricao)
               movelRequerido =Movel(nome=furnitureRequerido.nome,tempoUso=furnitureRequerido.tempoUso,id=furnitureRequerido.id,
               descricao=furnitureRequerido.descricao)
               propostas.append(Proposta(idProposta=proposta.idProposta,usuarioAlvo=usuarioAlvo,usuarioRequisitante=usuarioRequisitante
               ,movelProposto=movelProposto,movelRequerido=movelRequerido,status=proposta.status))
            return propostas
      except Exception as e :
         print(e,"saa")
         return None
    
    def cadastrarMovel(self,cpf:int, movel:Movel)-> int:
      try:
            stub = movel_pb2_grpc.MovelStub(self.channel)
            furniture= movel_pb2.Furniture(nome = movel.nome, tempoUso= movel.tempoUso,descricao=movel.descricao)
            criarMovel = movel_pb2.CriarMovel(movel=furniture,cpf=cpf)
            response = stub.criarMovel(criarMovel)
            return response.status
      except Exception as e:
         print(e)
         return None

    def excluirMovel(self,idMovel:int,cpf:int)-> int:
      try:
            stub = movel_pb2_grpc.MovelStub(self.channel)
            excluirMovel = movel_pb2.ExcluirMovel(cpf=cpf,idMovel=idMovel)
            response = stub.excluirMovel(excluirMovel)
            return response.status
      except Exception as e:
         print(e)
         return None
    
    def aceitarProposta(self,idProposta:int,cpfUsuario:int):
      try:
            stub = proposta_pb2_grpc.propostaStub(self.channel)
            aceitarProposta= proposta_pb2.AceitarProposta(id=idProposta,cpfUsuarioAlvo=cpfUsuario)
            response = stub.aceitarProposta(aceitarProposta)
            print(response.status)
            return response.status
      except Exception as e:
         print(e)
         return None

    def recusarProposta(self,idProposta:int,cpfUsuario:int):
      try:
            stub = proposta_pb2_grpc.propostaStub(self.channel)
            recusarProposta= proposta_pb2.AceitarProposta(id=idProposta,cpfUsuarioAlvo=cpfUsuario)
            response = stub.recusarProposta(recusarProposta)
            return response.status
      except Exception as e:
         print(e)
         return None
    
    def fazerProposta(self,cpfRequisitante:int,idMovelRequerido:int,idMovelProposto:int,
    cpfpassRequisitado:int):
      try:
            stub = proposta_pb2_grpc.propostaStub(self.channel)
            proposta = proposta_pb2.Proposta(idMovelRequerido=idMovelRequerido, 
            idMovelProposto = idMovelProposto,
            cpfUsuarioRequisitante= cpfRequisitante,
            cpfUsuarioRequisitado =  cpfpassRequisitado)
            response = stub.fazerProposta(proposta)
            return response.status
      except Exception as e:
         print(e)
         return None
    
 

