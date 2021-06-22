import BankingOperations
import UserSettings

#TELA DO USUÁRIO
def tela_usuario(nome_cliente):
    
    while(True):

        print(f"SEJA BEM VINDO(A) {nome_cliente} AO BANCO WTIC, DIGITE A OPERAÇÃO DESEJADA.\n")

        print("[1]Operações Bancárias")
        print("[2]Configurações do Usuário")
        print("Digite 'sair' se deseja fechar o programa\n")

        opcao = input("O QUE DESEJA FAZER?\n")

        if opcao.lower() == 'sair': #DIGITANDO ESSA OPÇÃO VOCÊ SAI DO CÓDIGO
            print("Até logo")
            exit(0)
        elif opcao == '1': #DIGITANDO ESSA OPÇÃO VOCÊ É ENCAMINHADO PARA AS OPERAÇÕES BANCÁRIAS
            BankingOperations.transações_bancárias(nome_cliente)
        elif opcao == '2': #DIGITANDO ESSA OPÇÃO VOCÊ É ENCAMINHADO PARA AS CONFIGURAÇÕES DO USUÁRIO
            UserSettings.configuracoes_sistema(nome_cliente)
        else: #QUALQUER OUTRA COISA DIGITADA SERÁ INVALIDADA PARA O BOM FUNCIONAMENTO DO CÓDIGO
            print("Opção inválida, tente novamente")
            continue