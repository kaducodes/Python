#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
print(str('Temos um Triângulo Retângulo...'))

#Forma 1
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f'Forma 1: O comprimento da Hipotenusa é {h:.2f}.')

#Forma 2
from math import sqrt
h2 = sqrt (co ** 2 + ca ** 2)
print(f'Forma 2: O comprimento da Hipotenusa é {h2:.2f}.')

#Forma 3
from math import hypot
h3 = hypot(co, ca)
print(f'Forma 3: O comprimento da Hipotenusa é {h3:.2f}.')
