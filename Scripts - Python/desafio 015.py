#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d1 = int(input('Por quantos dias o carro foi alugado? '))
q1 = float(input('Quantos kilometros o carro rodou no período? '))
d2 = int(d1 * 60)
q2 = float(q1 * 0.15)
print(f'O aluguel custou R$ {(d2 + q2):.2f}.')
