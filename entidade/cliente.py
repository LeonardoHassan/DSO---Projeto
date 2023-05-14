from entidade.pessoa import Pessoa

class Cliente(Pessoa):
  
    def __init__(self, nome: str, cpf: int, gastos_totais: float):
      super().__init__(nome, cpf)
      self.__gastos_totais = (float)(0)

    @property
    def gastos_totais(self):     
        return self.__gastos_totais

    @gastos_totais.setter
    def gastos_totais(self, gastos_totais):
        self.__gastos_totais = gastos_totais

cliente1 = Cliente("Joao", 1, 0 )
cliente2 = Cliente("Carlos", 2, 0)
cliente3 = Cliente("Pedro Sell", 3, 0)
cliente4 = Cliente("Marcos", 4, 0)
cliente5 = Cliente("Felipe", 5, 0)

lista_cliente = [cliente1,cliente2,cliente3,cliente4,cliente5]
