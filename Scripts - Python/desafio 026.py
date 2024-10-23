#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Qual letra você quer analisar na frase? ')).strip().upper()
print('A letra {} aparece {} vezes na frase.'.format(letra, frase.count(letra)))
print('A primeira letra {} apareceu na {}º posição'.format(letra, frase.find(letra)+1))
print('A última letra {} apareceu na {}º posição'.format(letra, frase.rfind(letra)+1))
