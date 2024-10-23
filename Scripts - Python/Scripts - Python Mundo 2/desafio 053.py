#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex.: APOS A SOPA
#A SACADA DA CASA
#O LOBO AMA BOLO
#ANOTARAM A DATA DA MARATONA
#Desconsiderando acentos e espaços
frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]'''
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
