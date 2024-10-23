#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
print('~' * 55)
print('Confederação Nacional de Natação - Classificação Atleta')
print('~' * 55)
ano = date.today().year
a = int(input('Digite o ano em que você nasceu: '))
c = ano - a
print(f'O Atleta tem {c} anos\nSua Categoria será:')
if c <= 9:
    print('Classificação: MIRIM')
elif c <= 14:
    print('Classificação: INFANTIL')
elif c <= 19:
    print('Classificação: JUNIOR')
elif c <= 25:
    print('Classificação: SÊNIOR')
elif c > 25:
    print('Classificação: MASTER')
