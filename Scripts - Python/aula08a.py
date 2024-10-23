#teste 01 - módulo math
from math import sqrt , ceil
num = int(input('Digite um número: '))
raiz = sqrt (num)
print(f'A raiz de {num} é igual a: {ceil(raiz)}.')

#teste 02 - módulo random
import random
n2 = random.randint(1, 10)
print(f'Seu múmero aleatório do momento é: {n2} e...')

#teste 03 - módulo extra externo: emoji
import emoji
print(emoji.emojize("Olá, mundo :sunglasses:", language='alias'))
print(emoji.emojize("Vamos que vamos! :smile:", language='alias'))

