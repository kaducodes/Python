#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Programa - Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeira segmento = '))
r2 = float(input('Segunda segmento = '))
r3 = float(input('Terceira segmento = '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos de reta PODEM formar um Triângulo!!')
else:
    print('Esses segmentos de reta NÃO PODEM formar um Triângulo.')
