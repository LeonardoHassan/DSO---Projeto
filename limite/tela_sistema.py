class TelaSistema:
   
    def tela_opcoes(self):
        print("-------- POSTO IPIrangoTANGO ---------")
        print("Escolha sua opcao")
        print("1 - Pessoas")
        print("2 - Bombas")
        print("3 - Produtos")    
        print("4 - Transações")
        print("0 - Finalizar sistema")
        opcao = input("Escolha a opcao: ")
        while not (opcao.isdigit()) or int(opcao) not in [1,2,3,4,0]:
            print("DIGITE UM VALOR VÁLIDO (1,2,3,4,0)")
            opcao = input("Escolha a opcao: ")
        return int(opcao)

    
