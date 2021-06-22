import BankingOperations
from datetime import datetime

#SAQUE
def realizando_saque(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo = saldo.read()
    saldo.close()
    saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

    print("<$>SAQUE<$>")
    print("Digite 'voltar' para voltar para as operações bancárias\n")

    sacar_dinheiro = input("Quanto você deseja sacar?\n")
    
    if sacar_dinheiro.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        saldo2.write(alterar_saldo)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return

    elif sacar_dinheiro.isnumeric() == False: #VALIDAÇÃO PRA QUE NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print("Digite uma quantia numérica\n")
        saldo2.write(alterar_saldo)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return

    else: #OPERAÇÃO EM SI SENDO EFETUADA

        abrir_senha=open(f'{nome_cliente}/senha.txt',"r")
        abrir_senha.close()

        sacar_dinheiro = int(sacar_dinheiro)
        alterar_saldo = int(alterar_saldo)

        if sacar_dinheiro > alterar_saldo: #SE A PEDIDA DO SAQUE FOR MAIOR DO Q O VALOR ATUAL NA CONTA O SAQUE NÃO SERÁ REALIZADO
            print("Dinheiro insuficiente pra realizar a transação!\n")
            alterar_saldo = str(alterar_saldo)
            saldo2.write(alterar_saldo)
            saldo2.close()
            BankingOperations.transações_bancárias(nome_cliente)
            return
        else: #SAQUE SENDO REALIZADO

            abrir_senha = open(f'{nome_cliente}/senha.txt',"r")
            ver_senha = abrir_senha.read()
            abrir_senha.close()
            verificar_senha = input('Digite sua senha para a confirmação.\n')
            while ver_senha!=verificar_senha:
                verificar_senha = input('Senha incorreta, digite novamente.\nDigite "voltar" para voltar às operações bancárias.\n')
                if verificar_senha.lower()=='voltar':
                    BankingOperations.transações_bancárias(nome_cliente)
                    return

            print("Saque realizado com sucesso!")
            alteracao = int(alterar_saldo) - int(sacar_dinheiro)
            alteracao = str(alteracao)
            saldo2.write(alteracao)
            saldo2.close()

            extrato = open(f'{nome_cliente}/extrato.txt','a')
            data = datetime.now()
            data_e_hora=data.strftime('%d/%m/%Y %H:%M')##TA FUNCIONANDO 26/11/2020 08:43
            extrato.write(f'{data_e_hora} - Saque de R${sacar_dinheiro} realizado.\n')
            extrato.close()
            BankingOperations.transações_bancárias(nome_cliente)
            return