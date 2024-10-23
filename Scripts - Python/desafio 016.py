#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex.: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
#Forma 1
r = float(input('Digite um número Real: '))
i = int(r)
print(f'Forma 1: O valor digitado foi {r} e a sua porção inteira é {i}.')

#Forma 2
from math import trunc
print(f'Forma 2: O valor digitado foi {r} e a sua porção inteira é {trunc(r)}.')
