#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep
print('{:=^54}'.format(' OLÁ '))
print('São pares os seguintes números no intervalo de 0 à 50:')
for c in range(2,51,2):
    sleep(0.2)
    print(c, end=' ')
