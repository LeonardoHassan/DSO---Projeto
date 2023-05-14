class TelaTransacao:

    def tela_opcoes(self):
        print("-------- TRANSAÇÕES ----------")
        print("Escolha uma opção")
        print("1 - Fazer Transação")
        print("2 - Listar Transações")
        print("3 - Excluir Transação")
        print("4 - Total vendido do posto")
        print("0 - Retornar")
        opcao = input("Escolha a opcao: ")
        while not (opcao.isdigit()) or int(opcao) not in [1,2,3,4,0]:
            print("DIGITE UM VALOR VÁLIDO (1, 2, 3, 4, 5, 0)")
            opcao = input("Escolha a opcao: ")
        return int(opcao)


    def pega_tipo_transacao(self):
        print("-------- TRANSAÇÃO ----------")
        cliente = input("Digite o CPF do cliente: ")
        while not (cliente.isdigit()):
            print("DIGITE UM VALOR VÁLIDO.")
            cliente = input("Digite o CPF do cliente: ")

        print("-----------------------\n1 - Combustível\n2 - Produto")
        tipo = input("-----------------------\nSelecione o tipo de transação: ")
        while not (tipo.isdigit()) or int(tipo) not in [1,2]:
            print("DIGITE UM VALOR VÁLIDO (1 ou 2).")
            print("-----------------------\n1 - Combustível\n2 - Produto")
            tipo = input("-----------------------\nSelecione o tipo de transação: ")

        return {"cliente": int(cliente), "tipo": int(tipo)}
    
    def transacao_produto(self):
        print("----------------------")
        produto = input("Selecione o produto pelo ID: ")
        while not (produto.isdigit()):
            print("DIGITE UM VALOR VÁLIDO.")
            produto = input("Selecione o produto pelo ID: ")

        quantidade = input("Selecione a quantidade: ")
        while not (quantidade.isdigit()):
            print("DIGITE UM VALOR VÁLIDO.")
            quantidade = input("Selecione a quantidade: ")

        return {"produto": int(produto), "quantidade": int(quantidade)}
    
    def transacao_bomba(self):
        print("----------------------")
        bomba = input("Selecione a bomba pelo numero: ")
        while not (bomba.isdigit()):
            print("DIGITE UM VALOR VÁLIDO.")
            bomba = input("Selecione a bomba pelo numero: ")     

        litros = input("Selecione quantos serão comprados: ")
        while not (litros.isdigit()):
            print("DIGITE UM VALOR VÁLIDO.")
            litros = input("Selecione quantos serão comprados: ")

        return {"bomba": int(bomba), "litros": int(litros)}

    def mostra_transacao(self, dados_transacao):
        print("--------------------------------")
        print("CLIENTE:", dados_transacao["cliente"])
        print("ID:", dados_transacao["id"])
        print("TIPO:", dados_transacao["tipo"])
        print("DESCRIÇÃO:", dados_transacao["descricao"])
        print("VALOR: R$", dados_transacao["valor"])
        print("\n")
    
    def seleciona_transacao(self):
        id = input("ID da transação que deseja: ")
        while not (id.isdigit()):
            print("DIGITE UM VALOR VÁLIDO.")
            id = input("ID da transação que deseja: ")
        return int(id)

    def mostra_mensagem(self, msg):
        print(msg)