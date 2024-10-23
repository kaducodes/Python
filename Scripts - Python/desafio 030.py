#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
print('PAR ou ÍMPAR')
n = int(input('Digite o número: '))
c = n % 2
if c == 0:
    print(f'{n} é PAR!!')
else:
    print(f'{n} é ÍMPAR!!')
print('Sei tudo e mais um pouco, não é?!')
#Como retirar o 0?
