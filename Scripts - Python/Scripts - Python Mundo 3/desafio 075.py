#Desenvolva um programa que leia 4 valores pelo teclado
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: '))
       )
#e guarde-os em uma tupla. No final, mostre:
print(f'Você digitou os valores {num}')
#A) Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {num.count(9)} vezes')
#B) Em que posição foi digitado o primeiro valor 3
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
#C) Quais foram os valores pares
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}',end=' ')