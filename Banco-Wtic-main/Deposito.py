import BankingOperations
from datetime import datetime

#DEPÓSITO

def realizando_deposito(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo = saldo.read()
    saldo.close()
    saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

    print("<$>DEPÓSITO<$>")
    print("Digite 'voltar' para voltar para as operações bancárias\n")

    depositar_dinheiro = input("Quanto você deseja depositar?\n")

    if depositar_dinheiro.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        saldo2.write(alterar_saldo)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return

    elif depositar_dinheiro.isnumeric() == False: #VALIDAÇÃO PRA QUE NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print("Digite uma quantia numérica\n")
        saldo2.write(alterar_saldo)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return

    else:
        
        abrir_senha = open(f'{nome_cliente}/senha.txt',"r")
        ver_senha = abrir_senha.read()
        abrir_senha.close()
        verificar_senha = input('Digite sua senha para a confirmação.\n')
        while ver_senha!=verificar_senha:
            verificar_senha = input('Senha incorreta, digite novamente.\nDigite "voltar" para voltar às operações bancárias.\n')
            if verificar_senha.lower()=='voltar':
                BankingOperations.transações_bancárias(nome_cliente)
                return

        #OPERAÇÃO EM SI SENDO EFETUADA
        print("Depósito realizado com sucesso!")
        alteracao = int(alterar_saldo) + int(depositar_dinheiro)
        alteracao = str(alteracao)
        saldo2.write(alteracao)
        saldo2.close()

        #Salvando no extrato
        extrato = open(f'{nome_cliente}/extrato.txt','a')
        data = datetime.now()
        data_e_hora=data.strftime('%d/%m/%Y %H:%M')##TA FUNCIONANDO 26/11/2020 08:43
        extrato.write(f'{data_e_hora} - Depósito de R${depositar_dinheiro} realizado.\n')
        extrato.close()

        BankingOperations.transações_bancárias(nome_cliente)
        return