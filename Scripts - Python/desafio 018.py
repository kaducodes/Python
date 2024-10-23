#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
a1 = float(input('Digite um ângulo: '))
a2 = radians(a1)
s = sin(a2)
c = cos(a2)
t = tan(a2)
print(f'O ângulo de {a1}º tem o SENO de {s:.2f}')
print(f'O ângulo de {a1}º tem o COSSENO de {c:.2f}')
print(f'O ângulo de {a1}º tem a TANGENTE de {t:.2f}')
