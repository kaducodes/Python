#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('*' * 14)
print('Cálculo de IMC')
print('*' * 14)
p = float(input('Digite seu peso (kg): '))
a = float(input('Digite sua altura (m): '))
imc = p / a ** 2
print(f'Seu IMC é de {imc:.1f}\nVocê está', end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO NORMAL')
elif 18.5 <= imc < 25:
    print('com o PESO IDEAL')
elif 25 <= imc < 30:
    print('com SOBREPESO')
elif 30 <= imc < 40:
    print('com OBESIDADE')
elif imc >= 40:
    print('com OBESIDADE MÓRBIDA')
