from entidade.tipoCombustivel import TipoCombustivel

class Bomba:
  def __init__(self,numero_bomba: int, tipo_combustivel: TipoCombustivel, capacidade: int, total_vendido: int):
      self.__numero_bomba: numero_bomba
      if (isinstance(tipo_combustivel, TipoCombustivel)):
          self.__tipo_combustivel: tipo_combustivel
      self.__capacidade: capacidade
      self.__total_vendido: total_vendido

  @property
  def numero_bomba(self):
    return self.__numero_bomba

  @property
  def tipo_combustivel(self):
    return self.__tipo_combustivel

  @tipo_combustivel.setter
  def tipo_combustivel(self, tipo_combustivel):
    self.__tipo_combustivel = tipo_combustivel

  @property
  def capacidade(self):
    return self.__capacidade

  @property
  def total_vendido(self):
    return self.__total_vendido
