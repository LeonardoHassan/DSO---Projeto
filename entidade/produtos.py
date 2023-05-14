class Produtos:
    def __init__(self, nome: str, preco: float, id: int, quantidade: int):
        self.__nome = nome
        self.__preco = preco
        self.__id = id
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def id(self):
        return self.__id

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade        

    

produto1 = Produtos("Bala", 1.00, 1, 10)
produto2 = Produtos("Cigarro", 10.25, 2, 15)
produto3 = Produtos("Cachaça", 25.00, 3, 5)
produto4 = Produtos("Chocolate", 6.75, 4, 8)
produto5 = Produtos("Energético", 15.50, 5, 30)

lista_produtos = [produto1,produto2,produto3,produto4,produto5]