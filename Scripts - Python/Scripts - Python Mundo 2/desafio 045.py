#Crie um programa que faça o computador jogar Jokenpô (Pedra, papel, tesoura) com você.

'''import random
print('=) ' * 14)
print('{:=^40}'.format(' JOKENPÔ '))
print('=) ' * 14)
v = str(input('Pedra, Papel ou Tesoura? ')).strip()
vm = v.upper()
lista = ['Pedra', 'Papel', 'Tesoura']
c = str(random.choice(lista))
print(f'{c}!!!!')
if c == 'Pedra' and vm == 'TESOURA':
    print('Arrá, Ganhei de você')
elif c == 'Pedra' and vm == 'PAPEL':
    print('Droga! Você ganhou de mim')
elif c == 'Pedra' and vm == 'PEDRA':
    print('Empate!')
elif c == 'Papel' and vm == 'PEDRA':
    print('Arrá, Ganhei de você')
elif c == 'Papel' and vm == 'TESOURA':
    print('Droga! Você ganhou de mim')
elif c == 'Papel' and vm == 'PAPEL':
    print('Empate!')
elif c == 'Tesoura' and vm == 'PAPEL':
    print('Arrá, Ganhei de você')
elif c == 'Tesoura' and vm == 'PEDRA':
    print('Droga! Você ganhou de mim')
elif c == 'Tesoura' and vm == 'TESOURA':
    print('Empate!')'''

from random import randint
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!!!!!')
sleep(0.3)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
