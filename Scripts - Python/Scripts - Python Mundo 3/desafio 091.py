#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#Jogadores sorteados:
    #O jogadorx tirou y
    #... ... ...
#Ranking dos jogadores:
    #1º lugar: jogadorx com y
    #... ... ...

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }

ranking = []

maior = 0
jogador = 0

print('Jogadores Sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()

print('-=' * 30)
print('  == Ranking dos Jogadores ==')

for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
