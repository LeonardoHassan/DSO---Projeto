class TipoCombustivel:

    def __init__(self, tipo: str, preco_litro: float, id_tipo: int):
        self.__tipo = tipo
        self.__preco_litro = preco_litro
        self.__id_tipo = id_tipo   

    @property
    def tipo(self):
      return self.__tipo    
    
    @property
    def preco_litro(self):
      return self.__preco_litro   
    
    @preco_litro.setter
    def preco_litro(self, preco_litro):
      self.__preco_litro = preco_litro    
      
    @property
    def id_tipo(self):
      return self.__id_tipo


gasolina = TipoCombustivel('Gasolina', 5.00, 1)
diesel = TipoCombustivel('Diesel', 4.25, 2)
etanol = TipoCombustivel('Etanol', 3.50, 3)

