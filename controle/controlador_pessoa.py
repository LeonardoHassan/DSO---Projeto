from entidade.funcionario import Funcionario
from entidade.cliente import Cliente
from limite.tela_pessoa import TelaPessoa

class ControladorPessoa:
    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__clientes = []
        self.__tela_bomba = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        print("Não era minha parte do trabalho")
        self.retornar

    def retornar(self):
        self.__controlador_sistema.abre_tela()
