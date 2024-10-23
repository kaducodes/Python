#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('=' * 35)
print('Programa de Validação de Empréstimo')
print('=' * 35)
v1 = float(input('Qual o valor do Imóvel? R$ '))
v2 = float(input('Qual o seu salário? R$ '))
v3 = int(input('Em quantos anos você pretende pagar o Empréstimo? '))
m = v3 * 12
p = v1 / m
if p <= 0.3 * v2:
    print('Parabéns! Seu Empréstimo foi Aprovado!')
    print(f'A sua parcela será de R$ {p:.2f}/mês durante {v3} anos.')
else:
    print('Infelizmente o seu Empréstimo não foi aprovado com esses dados, tente novamente!')
    print(f'A sua parcela seria de R$ {p:.2f}/mês e excederia os 30% (R$ {v2 * 0.3}) do seu salário.')
