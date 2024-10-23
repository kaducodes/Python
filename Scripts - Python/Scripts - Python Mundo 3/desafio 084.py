# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
#Nome:
#Peso:
#Quer continuar? [S/N]
#Você cadastrou x pessoas
#O maior peso foi de xxkg. Peso de x
#O menor peso foi de xkg. Peso de x
temporaria = [] #cria lista temporária para armazenar os dados
lista = [] #cria lista permanente para analisar os dados
maior = menor = 0 #cria as variáveis maior e menor para análise
while True:
    temporaria.append(str(input("Nome: "))) #adiciona nome ao slot 0
    temporaria.append(float(input("Peso: "))) #adiciona peso ao slot 1
    if len(lista) == 0: #se o tamanho da lista for zero, ou seja, estiver vazia...
        maior = menor = temporaria[1] #maior e menor serão o peso adicionado na lista temporária
    else: #senão, faz a análise e adiciona de acordo
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temp[1] < menor:
            menor = temporaria[1]
    lista.append(temporaria[:]) #faz uma cópia dos dados coletados
    temporaria.clear() #apaga a lista temporária
    resposta = str(input("Quer continuar? [S/N] ")).upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        print("Programa Finalizado")
        break
    else:
        print("Não reconheço sua resposta, presumo que queira finalizar...")
        break
print('-=' * 30)
print(f'Você cadastrou {len(lista)} pessoas') #o tamanho da lista pode ser substituído pelo clássico contador
print(f'Os dados foram {lista}')
print(f'O maior peso foi de {maior}kg. Peso de ', end='') #lembrando que a variável 'maior' só pegou o peso [1]
for p in lista:
    if p[1] == maior: #todos que tiverem o peso [1] igual ao maior...
        print(f'[{p[0]}] ', end='') #... aparecerão os nomes [0] correspondentes aqui
print() #para dar espaço
print(f'O menor peso foi de {menor}kg. Peso de ', end='') #lembrando que a variável 'menor' só pegou o peso [1]
for p in lista:
    if p[1] == menor: #todos que tiverem o peso [1] igual ao menor...
        print(f'[{p[0]}] ', end='') #... aparecerão os nomes [0] correspondentes aqui
print()
