#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados em ordem crescente.
#Digite um valor:
#Valor adicionado com sucesso...
#Quer continuar? [S/N]
#Valor duplicado! Não vou adicionar...
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
    elif resposta == 'S':
        continue
    else:
        print('Não reconheço essa resposta...')
lista.sort()
print('-='*30)
print(f'Esses são os valores digitados em ordem crescente: {lista}')


