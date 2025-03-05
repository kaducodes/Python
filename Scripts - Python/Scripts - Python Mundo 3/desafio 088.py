# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# Quantos jogos você quer que eu sorteie?
# Jogo x:
from random import randint
from time import sleep

lista = list()
jogos = list()
cont = 0

print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, end='')
print(f' SORTEANDO OS {quant} JOGOS ', end='')
print('-=' * 3)

for i, l in enumerate(jogos, 1):
    print(f'Jogo {i}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

    