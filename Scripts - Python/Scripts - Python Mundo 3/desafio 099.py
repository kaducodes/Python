#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    mai = 0
    tam = len(num)
    if num > mai:
        if num > maior:
            maior = num
    
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(num, end='')
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 1)

#verificar a lógica do maior