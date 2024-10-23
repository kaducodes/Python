#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.
print('Programa - Preço da Passagem')
d = float(input('Qual a distância (em Km) dessa viagem? '))
if d <= 200:
    v1 = d * 0.5
else:
    v1 = d * 0.45
print(f'Uma viagem de {d} Km custa R$ {v1:.2f}')
print('O(A) Senhor(a) deseja comprar?')
preço = d * 0.5 if d <= 200 else d * 0.45
print(f'Sim, o valor será R$ {preço:.2f}')
