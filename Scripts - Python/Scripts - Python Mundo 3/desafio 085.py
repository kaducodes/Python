# Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Digite o 1º Valor:
# Digite o 2º Valor:
# Digite o 3º Valor:
# Digite o 4º Valor:
# Digite o 5º Valor:
# Digite o 6º Valor:
# Digite o 7º Valor:
# Os valores pares digitados foram:
# Os valores ímpares digitados foram:
lista = []
numeros = []
cont = 0
for n in range (0,6):
    cont += 1
    n = float(input(f'Digite o {cont}º Valor: '))
    if n % 2 == 0:
        numeros.append(n)
    else:
        