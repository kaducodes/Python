#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.
print('Programa - Radar Eletrônico')
v = float(input('Qual velocidade em km/h você passou no Radar? '))
m = v % 80 * 7
if v > 80:
    print('Você foi multado em um valor de R$ {:.2f}.'.format(m))
else:
    print('Parabéns! Você está dirigindo com atenção! Continue assim!')
print('==============================================')