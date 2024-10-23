#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('Valor adicionado com sucesso')
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    else:
        print('Não reconheço essa resposta...')
        resposta = str(input('Você deseja continuar? [S/N] '))
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(lista)} números')
print(f'A lista dos números digitados em ordem decrescente é: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')

#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
#Digite um valor:
#Deseja continuar? [S/N]
