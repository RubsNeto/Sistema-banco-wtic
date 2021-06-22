#SALDO

def realizando_saldo(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo = saldo.read()
    saldo.close()

    print(f'{nome_cliente} seu saldo é de R${float(alterar_saldo)}\n')