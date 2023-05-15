from entidade.cliente import Cliente, lista_cliente
from limite.tela_transacao import TelaTransacao
from entidade.bomba import Bomba
from entidade.produtos import Produtos, lista_produtos
from controle.controlador_bomba import ControladorBomba
from entidade.transacao import Transacao
from exception import ExceptionTeste

class ControladorTransacao:
    def __init__(self, controlador_sistema):
        self.__transacoes = []
        self.__tela_transacao = TelaTransacao()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_bomba = self.__controlador_sistema.controlador_bomba

    def fazer_transacao (self):

        #Clientes é umas lista de objeto pré-pronta

        for cliente in lista_cliente:
            print("----------------\nNome do cliente: {}\nCPF: {}".format(cliente.nome,cliente.cpf))
        dados = self.__tela_transacao.pega_tipo_transacao()
        x = 0
        for cliente in lista_cliente:
            if (cliente.cpf == dados["cliente"]):
                dados["cliente"] = cliente
                x = 1  
                break  
        if x == 0:
            dados["cliente"] = None

        while dados["cliente"] is None:
            x = 0
            self.__tela_transacao.mostra_mensagem("Cliente não existente.")
            for cliente in lista_cliente:
                print("----------------\nNome do cliente: {}\nCPF: {}".format(cliente.nome,cliente.cpf))
            dados = self.__tela_transacao.pega_tipo_transacao()
            for cliente in lista_cliente:
                if cliente.cpf == dados["cliente"]:
                    dados["cliente"] = cliente
                    x = 1
                    break 
            if x == 0:
                dados["cliente"] = None
                    
        if len(self.__transacoes) == 0:
            id = 1
        else:
            id = int(self.__transacoes[len(self.__transacoes)-1].id +1)
 
        if dados["tipo"] == 1:
            dados["tipo"] = "Combustível"
            self.__controlador_bomba.lista_bombas()
            dados_bomba = self.__tela_transacao.transacao_bomba()
            bomba = self.__controlador_bomba.seleciona_bomba(dados_bomba["bomba"])

            while True:
                if bomba and dados_bomba["litros"] <= bomba.capacidade:
                    break
                if not bomba:
                    self.__tela_transacao.mostra_mensagem("Bomba não existente. ")
                if bomba and dados_bomba["litros"] > bomba.capacidade:
                    self.__tela_transacao.mostra_mensagem("Litros solicitados excedem a capacidade da bomba, digite um valor válido")
                self.__controlador_bomba.lista_bombas()
                dados_bomba = self.__tela_transacao.transacao_bomba()
                bomba = self.__controlador_bomba.seleciona_bomba(dados_bomba["bomba"])
                
            valor_total = float(bomba.tipo_combustivel.preco_litro) * float(dados_bomba["litros"])
            transacao = Transacao(dados["cliente"], id, dados["tipo"],
                                  "{} Litros de {}.".format(dados_bomba["litros"], bomba.tipo_combustivel.tipo), valor_total)
            bomba.total_vendido += (valor_total)
            self.__transacoes.append(transacao)
        else:

            #Produtos é umas lista de objeto pré-pronta

            dados["tipo"] = "Produto"
            for produto in lista_produtos:
                self.__tela_transacao.mostra_mensagem("----------------\nNome do produto: {}\nID: {}\nPreço: {}\nQuantidade: {}".format(produto.nome,produto.id,produto.preco,produto.quantidade))
            dados_produto = self.__tela_transacao.transacao_produto()
            x = 0
            for produto in lista_produtos:
                if produto.id == dados_produto["produto"]:
                    dados_produto["produto"] = produto
                    x = 1
                    break
            if x == 0:
                dados_produto["produto"] = None

            while dados_produto["produto"] is None:
                x = 0
                self.__tela_transacao.mostra_mensagem("Produto não existente.")
                for produto in lista_produtos:
                    self.__tela_transacao.mostra_mensagem("----------------\nNome do produto: {}\nID: {}\nPreço: {}\nQuantidade: {}".format(produto.nome,produto.id,produto.preco,produto.quantidade))
                dados_produto = self.__tela_transacao.transacao_produto()
                for produto in lista_produtos:
                    if produto.id == dados_produto["produto"]:
                        dados_produto["produto"] = produto
                        x = 1
                        break
                if x == 0:
                    dados_produto["produto"] = None

            valor_total = (dados_produto["produto"].preco) * (dados_produto["quantidade"])
            transacao = Transacao(dados["cliente"], id, dados["tipo"],
                                  "{} Unidades de {}.".format(dados_produto["quantidade"], dados_produto["produto"].nome), valor_total)
            self.__transacoes.append(transacao)

    def lista_transacoes(self):
        if not self.__transacoes:
            self.__tela_transacao.mostra_mensagem("--------------\nATENÇÃO: Nenhuma transação existe")
            return
        for transacao in self.__transacoes:
            self.__tela_transacao.mostra_transacao({"cliente": transacao.cliente.nome, "id": transacao.id, "descricao": transacao.descricao, 
                                             "tipo": transacao.tipo, "valor": transacao.valor})
    
    def excluir_transacao(self):
        self.lista_transacoes()
        id_transacao = self.__tela_transacao.seleciona_transacao()
        transacao = self.seleciona_transacao(id_transacao)
        if(transacao is not None):
            self.__transacoes.remove(transacao)
            self.lista_transacoes()
        else:
            raise ExceptionTeste("---------------\nTRANSAÇÃO NÃO EXISTENTE")

    def seleciona_transacao(self, numero: int):
        for transacao in self.__transacoes:
            if(transacao.id == numero):
                return transacao
        return None
    
    def total_vendido(self):
        total = 0
        for transacao in self.__transacoes:
            total += transacao.valor
        self.__tela_transacao.mostra_mensagem(("---------------\nTOTAL VENDIDO: R$ {}".format(total)))
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()



    def abre_tela(self):
        try:
            lista_opcoes = {1: self.fazer_transacao, 2: self.lista_transacoes, 3: self.excluir_transacao, 4: self.total_vendido, 0: self.retornar}

            continua = True
            while continua:
                lista_opcoes[self.__tela_transacao.tela_opcoes()]()
        except ExceptionTeste as e:
            self.__tela_transacao.mostra_mensagem(e.mensagem)