#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
print('Programa - Ano BISSEXTO')
a = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
dia = date.today().day
mês = date.today().month
ano = date.today().year
b = a % 4
c = a % 100
d = a % 400
if b == 0 and c != 0 or d == 0:
    print(f'{a} É um ano BISSEXTO!')
else:
    print(f'{a} NÃO É um ano BISSEXTO.')
print('=)')
print(f'Hoje é {dia}/{mês}/{ano}. Aproveite, terráqueo!!')
