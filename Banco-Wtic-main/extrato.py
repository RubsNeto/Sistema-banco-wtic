def ver_extrato(nome_cliente):

    abrir=open(f'{nome_cliente}/extrato.txt')
    extrato=abrir.read()
    abrir.close()

    print(extrato)
    