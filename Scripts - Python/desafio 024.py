#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
c1 = str(input('Em que cidade você nasceu: ')).strip()
c2 = c1.upper()
print('Será que existe a palavra "SANTO" nela?')
print('SANTO' in c2)

print('''Pera pera pera...
deixa eu ver... 
tem "SANTO" no começo mesmo??''')
print(c2[:5] == 'SANTO')
