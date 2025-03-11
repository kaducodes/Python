#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print()
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(2, 9, 4, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
