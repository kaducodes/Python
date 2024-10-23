#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {c + 1}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print('=-' * 30)
print(f'O MAIOR Valor digitado foi: {maior} na ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i + 1}º Posição')
print(f'O MENOR Valor digitado foi: {menor} na ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i + 1}º Posição')

lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if n > 0:
