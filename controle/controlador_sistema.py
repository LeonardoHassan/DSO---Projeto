from limite.tela_sistema import TelaSistema
from controle.controlador_bomba import ControladorBomba
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_produtos import ControladorProdutos
from controle.controlador_transacao import ControladorTransacao

class ControladorSistema:

    def __init__(self):
        self.__controlador_bomba = ControladorBomba(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controlador_transacao = ControladorTransacao(self)
        self.__tela_sistema = TelaSistema()
    

    def inicializa_sistema(self):
        self.abre_tela()

    def tela_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def tela_bomba(self):
        self.__controlador_bomba.abre_tela()

    def tela_produtos(self):
        self.__controlador_produtos.abre_tela()
      
    def tela_transacao(self):
        self.__controlador_transacao.abre_tela()


    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.tela_pessoa, 2: self.tela_bomba, 3: self.tela_produtos, 4: self.tela_transacao, 
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

