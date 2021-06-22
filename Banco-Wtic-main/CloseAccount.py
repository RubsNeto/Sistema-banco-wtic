import UserSettings
import MainScreen
import shutil

#ENCERRAR A CONTA

def finalizar_conta(nome_cliente):

    while(True):

        print("<!>ENCERRAR A CONTA<!>\n")

        opcao_encerrar = input("Você deseja encerrar essa conta?\n")

        if opcao_encerrar.lower() == 'não': #DIGITANDO ESSA OPÇÃO VOCÊ RETORNARÁ AS CONFIGURAÇÕES DO USUÁRIO
            UserSettings.configuracoes_sistema(nome_cliente)
            return
        elif opcao_encerrar.lower() == 'sim': #DIGITANDO AQUI VOCÊ PROSSEGUE COM O PROCESSO DE EXCLUSÃO DA SUA PASTA DE USUÁRIO
            senha_cliente = open(f'{nome_cliente}/senha.txt', "r")
            senha_atual = senha_cliente.read()
            senha_cliente.close()

            senha = input("Digite sua senha atual pra prosseguir(Depois de apagada, você não poderá recuperar a sua conta):\n")

            #AQUI A SENHA QUE VOCÊ DIGITA SERÁ COMPARADA A SENHA DA SUA PASTA
            if senha != senha_atual: 
                print("Senha incorreta")
                continue
            else:
                shutil.rmtree(nome_cliente)
                MainScreen.tela_entrada()
                return


