
from entidade.cliente import Cliente

class Transacao:
    def __init__(self, cliente: Cliente, id: int, tipo: str, descricao: str, valor: float):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__id = id
        self.__tipo = tipo
        self.__descricao = descricao
        self.__valor = valor
        
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao      