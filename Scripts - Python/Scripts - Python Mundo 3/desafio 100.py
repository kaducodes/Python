#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

lista = []

def sorteia(lista):
    print('Sorteando 5 valores de lista: ', end='')
    for n in range(1, 6):
        n = randint(0, 9)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    sleep(0.5)
    print(f'Somando os valores pares de {lista}, temos: {soma}')


#Programa principal
sorteia(lista)
somaPar(lista)
