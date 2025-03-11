#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#ex: escreva('Olá, Mundo!')

#saída: Olá, Mundo!

def escreva(frase):
    tamanho = len(frase) + 4
    print('~' * tamanho)
    print(f'  {frase}')
    print('~' * tamanho)


#Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')

