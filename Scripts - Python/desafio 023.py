#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834
#unidade: 4 dezena: 3 centena: 8 milhar: 1
import
n = str(input('Digite um número: '))
print(f'Analisando o número {n}:')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

print('''É... como não sabemos as condicionantes ainda,
Se digitarmos um número menor do que 1000 ali iria dar erro.
Quer ver? testa aí! Então dessa forma, a programação vai
ter que ser total na matemática! Vamos lá!!''')

n2 = int(input('Digite um número: '))
u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10
print(f'Agora sim! Analisando o número {n2}:')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
