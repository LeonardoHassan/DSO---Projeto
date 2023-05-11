from limite.tela_bomba import TelaBomba
from entidade.bomba import Bomba
from entidade.tipoCombustivel import TipoCombustivel, diesel, gasolina, etanol

class ControladorBomba:
    def __init__(self, controlador_sistema):
        self.__bombas = []
        self.__tela_bomba = TelaBomba()
        self.__controlador_sistema = controlador_sistema

    def incluir_bomba(self):
        dados_bomba = self.__tela_bomba.pega_dados_bomba()
        l = self.seleciona_bomba(dados_bomba["numero"])
        if l is None:
            dic = {1: gasolina, 2: diesel, 3: etanol}
            dados_bomba["tipo"] = dic[dados_bomba["tipo"]]
            bomba = Bomba(dados_bomba["numero"], dados_bomba["tipo"], dados_bomba["capacidade"], 1)
            self.__bombas.append(bomba)
        else:
            self.__tela_bomba.mostra_mensagem("ATENÇÃO: Bomba já registrada.")

    def alterar_bomba(self):
        self.lista_bombas()
        numero_bomba = self.__tela_bomba.seleciona_bomba()
        bomba = self.seleciona_bomba(numero_bomba)
        if(bomba is not None):
            novos_dados_bomba = self.__tela_bomba.pega_dados_bomba()
            dic = {1: gasolina, 2: diesel, 3: etanol}
            novos_dados_bomba["tipo"] = dic[novos_dados_bomba["tipo"]]
            bomba.tipo_combustivel = novos_dados_bomba["tipo"]
            bomba.capacidade = novos_dados_bomba["capacidade"]

            
        else:
            self.__tela_bomba.mostra_mensagem("ATENÇÃO: Bomba não existente")

    def lista_bombas(self):
        if not self.__bombas:
            self.__tela_bomba.mostra_mensagem("--------------\nATENÇÃO: Nenhuma bomba existe")
            return
        for bomba in self.__bombas:
            self.__tela_bomba.mostra_bombas({"numero": bomba.numero_bomba, "tipo": bomba.tipo_combustivel.tipo, 
                                             "capacidade": bomba.capacidade, "total": bomba.total_vendido})
    

            
    def excluir_bomba(self):
        self.lista_bombas()
        numero_bomba = self.__tela_bomba.seleciona_bomba()
        bomba = self.seleciona_bomba(numero_bomba)

        if(bomba is not None):
            self.__bombas.remove(bomba)
            self.lista_bombas()
        else:
            self.__tela_bomba.mostra_mensagem("-------------\nATENÇÃO: Bomba não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def seleciona_bomba(self, numero: int):
        for bomba in self.__bombas:
            if(bomba.numero_bomba == numero):
                return bomba
        return None
    
    def litros_vendidos(self):
        self.lista_bombas()
        vendas_totais = 0
        for bomba in self.__bombas:
            vendas_totais += bomba.total_vendido
        self.__tela_bomba.mostra_mensagem("-----------------\nTOTAL VENDIDO: R${:.2f}".format(vendas_totais))

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_bomba, 2: self.alterar_bomba, 3: self.lista_bombas, 4: self.excluir_bomba, 5: self.litros_vendidos, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_bomba.tela_opcoes()]()