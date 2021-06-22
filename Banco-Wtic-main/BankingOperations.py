import UserScreen
import Saque
import Deposito
import Transferencia
import Saldo
import extrato

#OPERAÇÕES BANCÁRIAS

def transações_bancárias(nome_cliente):

    while(True):

        print("---OPERAÇÕES BANCÁRIAS---\n")

        print("[1] Para sacar")
        print("[2] Para depositar")
        print("[3] Para fazer transferência")
        print("[4] Para ver seu saldo")
        print("[5] Para ver seu extrato")
        print("Digite 'voltar' para voltar pra tela de usuário\n")

        operacao = input("O que deseja fazer?\n")

        if operacao == '1': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O SAQUE
            Saque.realizando_saque(nome_cliente)
        elif operacao == '2': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O DEPÓSITO
            Deposito.realizando_deposito(nome_cliente)
        elif operacao == '3': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO UMA TRANSFERêNCIA
            Transferencia.realizando_transferencia(nome_cliente)
        elif operacao == '4': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO UMA CONSULTA DE SALDO
            Saldo.realizando_saldo(nome_cliente)
        elif operacao == '5': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O EXTRATO
            extrato.ver_extrato(nome_cliente)
        elif operacao.lower() == 'voltar': #DIGITANDO ESSA OPÇÃO VOCÊ RETORNA PRA TELA DE USUÁRIO
            UserScreen.tela_usuario(nome_cliente)
        else: #QUALQUER OUTRA COISA DIGITADA SERÁ INVALIDADA PARA O BOM FUNCIONAMENTO DO CÓDIGO
            print("Opção Inválida, tente novamente")