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
num = [[], []]
valor = 0
for c in range (1,8):
    valor = int(input(f'Digite o {c}º Valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')