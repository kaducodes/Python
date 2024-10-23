#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('--=--' * 10)
print('Jogo da advinhação!!')
print('--=--' * 10)
print('Vou pensar em um número de 0 a 5 e quero que você advinhe qual foi!')
c = randint(0 , 5)
n = int(input('E aí? qual foi o número que eu pensei? '))
print('Loading...')
sleep(1)
if n == c:
    print('Parabéns! Acertou!! foi {} mesmo!!'.format(c))
else:
    print('Errouuuuuuuuu! Pensei no {}!!'.format(c))
print('E fim de papo!')
