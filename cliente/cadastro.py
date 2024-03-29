from cliente.cores import Cores
from middleware.cliente_midd import ClienteMidd
from models.usuario import Usuario

class Cadastro:
    def __init__(self) -> None:
        pass
    def menu(self,) -> int:
        cores = Cores()
        cliente=ClienteMidd()
        print(cores.criarTextoTela("---------- TELA DE CADASTRO ----------"))
        print()
        print("Insira os seus dados abaixo:")
        nome = input(cores.criarTextoOpcoes("Nome: "))
        cpf = int(input(cores.criarTextoOpcoes("CPF: ")))
        senha = input(cores.criarTextoOpcoes("Senha: "))
        usuario = Usuario(nome=nome,cpf=cpf,senha=senha)
        print()
        print(cores.criarTextoTela("---------- FIM TELA DE CADASTRO ----------"))
        print()
        return cliente.criarUsuario(usuario=usuario)