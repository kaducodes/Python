#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS OLIVEIRA '))
v = float(input('Digite o preço normal do produto: R$ '))
print('''Opçôes de Pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual será a Opção? '))
if opção == 1:
    p = v * 0.9
    print(f'Com 10% de desconto, R$ {p}')
elif opção == 2:
    p = v * 0.95
    print(f'Com 5% de desconto, R$ {p}')
elif opção == 3:
    p = v / 2
    print(f'Sem desconto, R$ {v}')
    print(f'Sua compra em 2x fica R$ {p}/mês')
elif opção == 4:
    p = v * 1.2
    parcelas = int(input('Quantas parcelas serão? '))
    p2 = p / parcelas
    print(f'Sua compra em {parcelas}x fica R$ {p2:.2f}/mês.')
    print(f'Sua compra de R$ {v} ficará R$ {p} no final.')
else:
    print('Opção Inválida de Pagamento')
