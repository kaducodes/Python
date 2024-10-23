#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues
#OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''print('='*40)
print('{:^30}'.format('BANCO CEV'))
print('='*40)
ced50 = ced20 = ced10 = ced1 = resto50 = resto20 = resto10 = resto1 = 0
while True:
    valor = int(input('Que valor você quer sacar? R$ '))
    ced50 = valor // 50
    resto50 = valor % 50
    if ced50 != 0:
        print(f'Total de {ced50} cédulas de R$ 50,00')
    if resto50 != 0:
        ced20 = resto50 // 20
        resto20 = resto50 % 20
        if ced20 != 0:
            print(f'Total de {ced20} cédulas de R$ 20,00')
    if resto20 != 0:
        ced10 = resto20 // 10
        resto10 = resto20 % 10
        if ced10 != 0:
            print(f'Total de {ced10} cédulas de R$ 10,00')
    if resto10 != 0:
        ced1 = resto10 // 1
        if ced1 != 0:
            print(f'Total de {ced1} cédulas de R$ 1,00')
    break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

