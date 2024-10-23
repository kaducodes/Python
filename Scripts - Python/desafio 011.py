#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
import math
l = float(input('Qual a Largura da parede? '))
h = float(input('Qual a Altura da parede? '))
a = float(l * h)
r = float(a / 2)
lata = math.ceil(float(r / 18))
gal = math.ceil(float(r / 3.6))
print(f'Você irá precisar de {r:.2f} Litros de tinta para pintar sua parede de {a:.2f} m².')
print(f'Portanto, precisará:\n{lata:.0f} Latas 18l;\nOu\n{gal:.0f} Galões 3,6l')
