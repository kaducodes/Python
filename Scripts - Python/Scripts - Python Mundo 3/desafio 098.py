#Faça um programa que tenha uma função chamada contador() que receba 3 parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar 3 contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

import time

def linhas():
    print('-=' * 30)

def contador(inicio, fim, passo):
    if fim > 0:
        print(f'Contagem de {inicio} até {fim-1} de {passo} em {passo}')
    else:
        print(f'Contagem de {inicio} até {fim+1} de {passo*-1} em {passo*-1}')
    if passo == 0:
        passo = 1
    for i in range(inicio, fim, passo):
        print(f'{i} ', end='')
        time.sleep(0.5)
    print('FIM!')

linhas()
contador(1, 11, 1)
linhas()
contador(10, -1, -2)
linhas()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
