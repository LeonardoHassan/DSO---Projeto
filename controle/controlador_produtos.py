from entidade.produtos import Produtos
from limite.tela_produtos import TelaProdutos

class ControladorProdutos:
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__tela_produtos = TelaProdutos()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        print("Não era minha parte do trabalho")
        self.retornar

    def retornar(self):
        self.__controlador_sistema.abre_tela()
