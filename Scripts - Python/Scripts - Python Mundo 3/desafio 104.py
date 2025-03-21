#Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

#ex.: n = leiaInt('Digite um número: ')
#Você acabou de digitar o número 3
#ERRO: Digite um número inteiro válido

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO: Digite um número inteiro válido\033[m]')
        if ok:
            break
    return valor
        

#main
print('-'* 40)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')