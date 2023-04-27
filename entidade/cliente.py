from entidade.pessoa import Pessoa

class Cliente(Pessoa):
  
  def __init__(self, nome: str, cpf: int, gastos_totais: int):
      super().__init__(nome, cpf)
      self.__gastos_totais: gastos_totais

  @property
  def gastos_totais(self):
      return self.__gastos_totais
