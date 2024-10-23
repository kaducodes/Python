#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('=' * 31)
print('Programa de Alistamento Militar')
print('*' * 31)
ano = date.today().year
a = int(input('Digite o ano que você nasceu: '))
idade = ano - a
print(f'Quem nasceu em {a} tem {idade} anos em {ano}.')
if idade < 17:
    i2 = 18 - idade
    print(f'Você falta {i2} anos para se alistar.')
    print(f'Seu alistamento será em {ano + i2}')
elif idade == 17:
    print('Você falta apenas 1 ano para se alistar.')
    print(f'Seu alistamento será em {ano + 1}')
elif idade == 18:
    print('Você tem que se alistar esse ano.')
elif idade == 19:
    print('Você passou do prazo de se alistar em 1 ano.')
    print(f'Seu alistamento foi em {ano - 1}')
else:
    i2 = idade - 18
    print(f'Você passou do prazo de se alistar em {i2} anos.')
    print(f'Seu alistamento foi em {ano - i2}')
