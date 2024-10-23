#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Qual o preço do produto? '))
d = float(input('Quantos porcento de desconto o produto terá? '))
p2 = p1 * (1 - d/100)
print(f'O produto passará a custar R$ {p2:.2f} com {d}% de desconto.')
