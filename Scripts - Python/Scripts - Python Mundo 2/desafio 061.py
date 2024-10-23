#Refaça o desafio 051, lendo o primeito termo e a razão de uma PA, mostrando os 10 primeiros termos da PA usando while
primeiro = int(input('1º Termo da PA: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM')




