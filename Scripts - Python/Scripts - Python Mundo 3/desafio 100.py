#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

lista = []
soma = 0

def sorteia(lista):
    for n in range(1, 6):
        n = randint(0, 9)
        lista.append(n)
        print(n, end=' ')
    print('PRONTO!')

def somaPar(* lista):
    print(f'Somando os valores pares de {lista}, temos: ', end='')
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)


    

sorteia(lista)
somaPar(lista)

#verificar a lógica da soma