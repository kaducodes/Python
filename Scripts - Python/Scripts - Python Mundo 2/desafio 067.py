#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tab < 0:
        break
    for c in range (1,11):
        print(f'{tab} * {c} = {tab * c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')