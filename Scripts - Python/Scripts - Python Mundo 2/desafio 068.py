#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    valor = int(input('Diga um valor: '))
    n = ' '
    pc = randint(0,10)
    soma = valor + pc
    resto = soma % 2
    while n not in 'PI':
        n = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {valor} e o computador {pc}, Total de {soma} ',end='')
    print('DEU PAR' if resto == 0 else 'DEU ÍMPAR')
    if n == 'P' and resto == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    if n == 'I' and resto != 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    if n == 'P' and resto != 0:
        break
    if n == 'I' and resto == 0:
        break
    cont += 1
print('Você PERDEU!')
print('-='*20)
print(f'GAME OVER! Você venceu {cont} vezes')
