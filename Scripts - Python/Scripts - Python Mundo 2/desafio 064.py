#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''soma = 0
n = 0
qtd = 0
while n != 999:
    n = int(input('Digite um número (Flag = 999): '))
    if n != 999:
        soma = soma + n
        qtd += 1
    if n == 999:
        print('Ok...')
print(f'A soma dos {qtd} números digitados antes do flag é {soma}')
print('Programa Finalizado')'''







soma = qtd = num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    qtd += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {qtd} números e a soma entre eles é {soma}')

