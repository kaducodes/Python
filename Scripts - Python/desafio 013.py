#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s1 = float(input('Qual o salário atual do funcionário? '))
a = float(input('De quantos porcento vai ser o aumento do salário desse funcionário? '))
s2 = float(s1 * (1 + a/100))
print(f'O salário será de R$ {s2:.2f} com o aumento de {a:.2f}%.')
