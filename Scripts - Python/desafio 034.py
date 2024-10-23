#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
print('Programa - Aumento salarial')
salario = float(input('Qual o seu salário atual? R$ '))
if salario > 1250:
    reajuste = salario * 1.1
    print(f'Seu Salário de R$ {salario} terá um reajuste de 10% e passará a ser R$ {reajuste:.2f}')
else:
    reajuste = salario * 1.15
    print(f'Seu Salário de R$ {salario} terá um reajuste de 15% e passará a ser R$ {reajuste:.2f}')
print('Parabéns pela promoção!!!')'''
