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
        lista_opcoes = {1: self.incluir_livro, 2: self.alterar_livro, 3: self.lista_livro, 4: self.excluir_livro, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_livro.tela_opcoes()]()