#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[33m', end=' ')
        print(c, end=' ')
    else:
        print('\033[31m', end=' ')
        print(c, end=' ')

print(f'\n\033[mO número {num} foi dividido {cont} vezes')
if cont == 2:
    print('E por isso ele \033[33mÉ PRIMO!')
else:
    print('E por isso ele \033[31mNÃO É PRIMO!')
