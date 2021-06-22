import os
import Login
import Tratamentos
import MainScreen
#TELA DE CADASTRO

def registro_pessoal():

    print("-------REGISTRO DO BANCO WTIC-------")

    #RECEBENDO E VALIDANDO NOME_ok
    nome_register = input("Digite o seu nome de usuário (este nome vai representar você em todas as ocasiões):\n")
    nome_register = Tratamentos.validando_nome(nome_register)
    
    #RECEBENDO E VALIDANDO IDADE_ok
    idade_register = input("Digite a sua idade:\n")
    idade_register = Tratamentos.validando_idade(idade_register)

    #RECEBENDO E VALIDANDO CPF_ok
    cpf_register = input("Digite seu cpf:\n")
    cpf_register = Tratamentos.validando_cpf(cpf_register)

    #RECEBENDO A SENHA
    senha_register = input("Digite sua senha:\n")

    #RECEBENDO E VALIDANDO SALDO
    saldo_register = input("Digite a quantidade a ser depositada:\n")
    saldo_register = Tratamentos.validando_saldo(saldo_register)

    #CRIAÇÃO DA PASTA
    pasta_cliente = f'{nome_register}'
    os.mkdir(pasta_cliente)

    #COLOCA A IDADE DENTRO DE UM ARQUIVO NA PASTA
    arquivo_idade = open(f'{pasta_cliente}/idade.txt',"w")
    arquivo_idade.write(idade_register)
    arquivo_idade.close()

    #COLOCA O CPF DENTRO DE UM ARQUIVO NA PASTA
    arquivo_cpf = open(f'{pasta_cliente}/cpf.txt',"w")
    arquivo_cpf.write(cpf_register)
    arquivo_cpf.close()

    #COLOCA A SENHA DENTRO DE UM ARQUIVO NA PASTA
    arquivo_senha= open(f'{pasta_cliente}/senha.txt',"w")
    arquivo_senha.write(senha_register)
    arquivo_senha.close()

    #COLOCA O NOME DENTRO DE UM ARQUIVO NA PASTA
    arquivo_nome= open(f'{pasta_cliente}/nome.txt',"w")
    arquivo_nome.write(nome_register)
    arquivo_nome.close()

    #COLOCA A QUANTIDADE DEPOSITADA DENTRO DE UM ARQUIVO NA PASTA
    arquivo_saldo= open(f'{pasta_cliente}/saldo.txt',"w")
    arquivo_saldo.write(saldo_register)
    arquivo_saldo.close()

    #SALVA O EXTRATO DENTRO DE UM ARQUIVO NA PASTA
    arquivo_extrato= open(f'{pasta_cliente}/extrato.txt',"w")
    arquivo_extrato.close()

    entrar = input("Cadastro efetuado com sucesso, deseja fazer login?\n")

    while(True):
        if entrar.lower() == 'sim': #DIGITANDO ESSA OPÇÃO VOCÊ SERÁ ENCAMINHADO PARA O LOGIN
            Login.entrar_programa()
            return
        elif entrar.lower() == 'não': #DIGITANDO ESSA OPÇÃO VOCÊ VOLTARÁ PARA A TELA PRINCIPAL
            MainScreen.tela_entrada()
            return
        else: #QUALQUER OUTRA COISA DIGITADA SERÁ INVALIDADA PARA O BOM FUNCIONAMENTO DO CÓDIGO
            entrar = input("Opção inválida, tente novamente.\n")