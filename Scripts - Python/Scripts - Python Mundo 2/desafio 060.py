#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#ex.: 5! = 5x4x3x2x1 = 120
from math import factorial
num = int(input('Digite um número: '))
print(f'{num}! = ',end='')
x = num
'''fatorial = factorial(num)'''
fatorial = 1
while x > 0:
    print(f'{x}',end='')
    print(' x ' if x > 1 else ' = ', end='')
    fatorial *= x
    x -= 1
print(f'{fatorial}')

