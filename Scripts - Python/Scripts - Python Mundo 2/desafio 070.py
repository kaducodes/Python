#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar
#No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$ 1.000,00.
#C) Qual é o nome d produto mais barato.
print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)
total = mil = cont = menor = 0
nmenor = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        nmenor = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'S':
        continue
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da sua compra foi R$ {total:.2f}')
print(f'Temos {mil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {nmenor} que custa R$ {menor:.2f}')
