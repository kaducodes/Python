#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00=R$3,27
r = float(input('Quantos Reais você tem na carteira? '))
d = float(r / 3.27)
print(f'Você pode comprar US$ {d:.2f} com R$ {r}')
