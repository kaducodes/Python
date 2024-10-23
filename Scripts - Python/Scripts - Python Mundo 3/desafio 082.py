#Crie um programa que vai ler vários números e colocar em uma lista.
lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('Valor adicionado com sucesso...')
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    else:
        print('Não reconheço sua resposta...')
        resposta = str(input('Deseja continuar? [S/N] ')).upper()
print(f'Lista GERAL: {lista}')
print(f'Lista de Valores PARES: {pares}')
print(f'Lista de Valores ÍMPARES: {impares}')
#Depois disso, crie 2 listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das 3 listas geradas.
#Digite um valor:
#Deseja continuar? [S/N]