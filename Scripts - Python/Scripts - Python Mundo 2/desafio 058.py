#Melhore o jogo do DESAFIO 028 ondeo computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('Sou seu computador...\nAcabei de pensar em um número de 0 a 10')
print('Será que você consegue adivinhar qual foi?')
pc = randint(0, 11)
acertou = False
tentativa = 0
user = int(input('Qual é o seu palpite? '))
while not acertou:
    tentativa += 1
    if user == pc:
        acertou = True
    else:
        if user > pc:
            user = int(input('Menos... Tente mais uma vez: '))
        if user < pc:
            user = int(input('Mais... Tente mais uma vez: '))
print(f'Acertou com {tentativa} tentativas. Parabéns!')
