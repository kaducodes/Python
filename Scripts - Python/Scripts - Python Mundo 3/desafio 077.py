#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

#Define uma tupla contendo as palavras.
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR', 'PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáãâeéêiíoôu':
            print(f'{letra.lower()} ', end='')
