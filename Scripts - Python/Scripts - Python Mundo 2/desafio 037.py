#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal, 3 para hexadecimal

print('=' * 21)
print('Programa de Conversão')
print('=' * 21)
n = int(input('Digite um Número Inteiro: '))
print('''Escolha a opção para Conversão em:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
c = int(input('Sua opção: '))
if c == 1:
    print(f'{n} convertido para BINÁRIO é: {bin(n)[2:]}')
elif c == 2:
    print(f'{n} convertido para OCTAL é: {oct(n)[2:]}')
elif c == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente!')
