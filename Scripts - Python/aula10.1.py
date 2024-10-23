#Condições Simples e Compostas
'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('Sim!! Carro novo!' if tempo <=3 else 'Sim!! Carro velho!')
cor = str(input('Qual a cor do seu carro? ')).strip().lower()
if cor == 'vermelho':
    print('Que cor legal pra carro!!')
else:
    print('Hum')
print('==FIM==')'''

print('Programa - Média Escolar')
m = float(input('Em primeiro lugar... Qual a média adotada pelo Colégio? '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
mc = (n1 + n2) / 2
r = m - mc
if mc >= 6:
    print('Parabéns! Você passou!')
else:
    print(f'Nota insuficiente, você irá para a recuperação precisando de {r:.2f} para passar.')
    print('Estude!!!!!!')




