import Login
import Register

#TELA INICIAL
def tela_entrada():

    while(True):

        print("-------BANCO WTIC-------\n")

        print("[1]Login")
        print("[2]Cadastro")
        print("Digite 'sair' se deseja fechar o programa\n")

        opcao = input("O QUE DESEJA FAZER?\n")

        if opcao.lower() == 'sair': #DIGITANDO ESSA OPÇÃO ELE SAI DO PROGRAMA
            print("Até logo")
            exit(0)
        elif opcao == '1': #DIGITANDO ESSA OPÇÃO VOCÊ É LEVADO PARA A TELA DE LOGIN
            Login.entrar_programa()
        elif opcao == '2': #DIGITANDO ESSA OPÇÃO VOCÊ É LEVADO PRA TELA DE CADASTRO
            Register.registro_pessoal()
        else: #SE NENHUMA DAS OPÇÕES ACIMA FOR SELECIONADA ELE RETORNA PEDINDO UMA INFORMAÇÃO VÁLIDA
            print("Opção inválida, tente novamente")
            continue