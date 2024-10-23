#Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores.
#Maioridade: 21 anos.
from datetime import date
atual = date.today().year
s = 0
for c in range (1,8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        s += 1
print(f'Ao todo tivemos {s} Pessoas maiores de idade\nE também tivemos {7 - s} pessoas menores de idade')

