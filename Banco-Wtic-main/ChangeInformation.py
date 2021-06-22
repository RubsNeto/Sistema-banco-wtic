import os,sys
import MainScreen
#ALTERAR INFORMAÇÕES PESSOAIS

def alteracao_informacoes(nome_cliente):


    abrir_senha=open(f'{nome_cliente}/senha.txt','r')
    senha_antiga=abrir_senha.read()
    abrir_senha.close()

    print("<!>ALTERAR INFORMAÇÕES PESSOAIS<!>")
    print("- Usuário")
    print("- Senha")

    informação = input("Que informação você deseja mudar?\n")

    if informação.lower() == 'usuario':

        nome=input('Qual o seu novo nome de usuário?\n')

        ver=input('Digite sua senha para confirmar o processo.\n')
        while senha_antiga!=ver:
            ver=input('Senha incorreta, tente novamente.\n')

        os.rename(f"{nome_cliente}" , f"{nome}")

        nome_antigo=open(f'{nome}/nome.txt','w')
        nome_antigo.write(f'{nome}')
        nome_antigo.close()

        print('Nome alterado com sucesso! faça o login novamente para atualização no sistema.\n')
        MainScreen.tela_entrada()
        return

    if informação.lower() == 'senha':
            
        nova_senha=input('Digite sua nova senha.\n')
            
        ver=input('Digite sua senha antiga para confirmar o processo.\n')
        while senha_antiga!=ver:
            ver=input('Senha incorreta, tente novamente.\n')
            
        alterar_senha=open(f'{nome_cliente}/senha.txt','w')
        alterar_senha.write(nova_senha)
        alterar_senha.close()
        print('senha alterada com sucesso!')
                