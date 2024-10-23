#Crie um programa que vai gerar 5 números aleatórios
#e colocar em uma tupla

#Depois disso, mostre a listagem de números gerados
#e também indique o menor e o maior valor que estão na tupla

from random import randint
a1 = randint(0,9)
a2 = randint(0,9)
a3 = randint(0,9)
a4 = randint(0,9)
a5 = randint(0,9)
numeros = (a1, a2, a3, a4, a5)
print(f'Os valores sorteados foram: {a1}, {a2}, {a3}, {a4} e {a5}')
print(f'O Maior número gerado foi: {max(numeros)}')
print(f'O Menor número gerado foi: {min(numeros)}')

# Pode fazer dessa forma também:
numero = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print('Os valores sorteados foram: ', end='')
for n in numero:
    print(f'{n} ', end='')
print(f'\nO Maior número gerado foi: {max(numero)}')
print(f'O Menor número gerado foi: {min(numero)}')

