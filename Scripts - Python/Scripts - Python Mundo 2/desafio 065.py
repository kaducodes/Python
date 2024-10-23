#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer continuar a digitar valores.
valor = maior = menor = cont = soma = 0
pergunta = 'S'
while pergunta in 'Ss':
    valor = int(input('Digite um número: '))
    cont += 1
    soma += valor
    if cont == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('Programa Finalizado!')
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor {menor}')



'''valor = int(input('Digite um valor: '))
resp = 'S'
qtd = 1
soma = valor
maior = 0
menor = valor
while resp == 'S':
    valor = int(input('Digite um valor: '))
    resp = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    qtd += 1
    soma = soma + valor
    maior = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
média = soma / qtd
print(f'A média entre os {qtd} valores digitados foi de {média:.2f}')
print(f'O maior número foi {maior} e o menor número foi {menor}')'''
