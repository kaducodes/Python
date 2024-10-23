#Crie um programa que tenha uma tupla
#totalmente preenchida com uma contagem
#por extenso, de zero até vinte.

#Seu programa deverá ler um número pelo teclado (entre 0 e 20)
#e mostrá-lo por extenso

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Seu número não está no intervalo. Tente novamente!')
print(f'Você digitou o número {extenso[numero]}')
