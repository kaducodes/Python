#Escreva um programa que leia um número n inteiro qualquer e
#mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
#ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''n = int(input('Quantos termos na Sequência de Fibonacci: '))
cont = 2
t1 = 0
t2 = 1
print('~~' * 20)
print(f'{t1} -> {t2} -> ', end='')
while cont < n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~~' * 20)'''

n = int(input('Quantos termos na Sequência de Fibonacci: '))
t1 = 1
t2 = 0
t = 0
cont = 2
print(f'{t2} -> {t1} -> ', end='')
while cont < n:
    cont += 1
    t = t1 + t2
    print(f'{t} - > ', end='')
    t2 = t1
    t1 = t
print('FIM')