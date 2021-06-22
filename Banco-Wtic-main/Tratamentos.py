#REGISTROS

def validando_nome(nome): #TRATAMENTO DE ERROS DE NOME

    while(True):

        while nome.isnumeric() == True:
            nome = input("Nome inválido, digite novamente\n")

        try:
            open(f'{nome}/nome.txt')
            nome = input("Nome já existente, digite novamente\n")

        except:
            return nome

def validando_idade(idade): #TRATAMENTOS DE ERROS DE IDADE
    while (idade.isnumeric() == False) or (int(idade) < 18):
            idade = input("Idade inválida, digite novamente.\n")

    return idade

def validando_saldo(saldo): #TRATAMENTO DE ERROS DO SALDO
    while (saldo.isnumeric()==False) or (int(saldo) < 0):
        saldo=input("Quantia inválida, digite novamente\n")

    return saldo

def validando_cpf(cpf):
    
    roda=True
    while(roda):

        while cpf.isnumeric()==False or (len(cpf) != 11):
            cpf=input('Cpf inválido, digite novamente.\n')

        lista=list(cpf)

        cont_crescente=0
        cont_decrescente=9
        crescente=0
        decrescente=0

        while cont_crescente!=9:
            
            crescente+=int(lista[cont_crescente])*(cont_crescente+1)
            decrescente+=int(lista[cont_decrescente])*(cont_decrescente)

            cont_crescente += 1
            cont_decrescente -= 1

        if crescente%11==10:
            crescente=0
        
        else:
            crescente=crescente%11

        if decrescente%11==10:
                decrescente=0
        
        else:
            decrescente=decrescente%11
        
        
        if int(lista[9])==crescente and int(lista[10])==decrescente:
            roda=False
            print(lista[9])
            print(lista[10])
            return cpf

        else:
            cpf=input('Cpf informado inválido, tente novamente\n')
#######################################################################
