class TelaBomba:
    
    def tela_opcoes(self):
        print("-------- AMIGOS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Bomba")
        print("2 - Alterar Bomba")
        print("3 - Listar Bombas")
        print("4 - Excluir Bombas")
        print("5 - Litros Vendidos")
        print("0 - Retornar")
        opcao = input("Escolha a opcao: ")
        while not (opcao.isdigit()):
            print("DIGITE UM NUMERO VÁLIDO")
            opcao = input("Escolha a opcao: ")
        while int(opcao) not in [1,2,3,4,5,0]:
            print("DIGITE UM VALOR VÁLIDO (1,2,3,4,5,0)")
            opcao = input("Escolha a opcao: ")
        return int(opcao)

    def pega_dados_bomba(self):
        print("\n--------- DADOS BOMBA ---------")
        numero_bomba = input("Numero: ") 
        while not (numero_bomba.isdigit()):
            print("DIGITE UM NUMERO VÁLIDO")
            numero_bomba = input("Numero: ")
        tipo_combustivel = (input("-----------------------\nGasolina - 1\nDiesel - 2\nEtanol -3\n-----------------------\nTipo de combustivel: "))
        while not (tipo_combustivel.isdigit()):
            print("DIGITE UM NUMERO VÁLIDO")
            tipo_combustivel = (input("-----------------------\nGasolina - 1\nDiesel - 2\nEtanol -3\n-----------------------\nTipo de combustivel: "))
        while int(tipo_combustivel) not in [1,2,3]:
            print("DIGITE UM VALOR VÁLIDO (1,2,3)")
            tipo_combustivel = (input("-----------------------\nGasolina - 1\nDiesel - 2\nEtanol -3\n-----------------------\nTipo de combustivel: "))
        capacidade = input("Capacidade da bomba (em litros): ")
        while not (capacidade.isdigit()):
            print("DIGITE UM NUMERO VÁLIDO")
            capacidade = input("Capacidade da bomba (em litros): ")
            

        return {"numero": int(numero_bomba), "tipo": int(tipo_combustivel), "capacidade": int(capacidade)}
    
    def mostra_bombas (self, dados_bomba):
        print("----------------------------")
        print("NUMERO DA BOMBA:", dados_bomba["numero"])
        print("TIPO DE COMBUSTIVEL:", dados_bomba["tipo"])
        print("CAPACIDADE DA BOMBA:", dados_bomba["capacidade"])
        print("TOTAL VENDIDO: R$", dados_bomba["total"])
        print("\n")

    def seleciona_bomba(self):
        numero = input("Numero da bomba: ")
        while not (numero.isdigit()):
            print("DIGITE UM NUMERO VÁLIDO")
            numero = input("Numero da bobma: ")
        return int(numero)
    
    def mostra_mensagem(self, msg):
        print(msg)