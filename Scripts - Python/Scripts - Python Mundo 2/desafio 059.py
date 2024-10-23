#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
v1 = float(input('Digite o valor 1: '))
v2 = float(input('Digite o valor 2: '))
s = 0
while s != 5:
    print('''    [1] somar  
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    s = int(input('>>>>> Qual a sua opção? '))
    if s == 1:
        r = v1 + v2
        print(f'{v1} + {v2} = {r}')
        continue
    if s == 2:
        r = v1 * v2
        print(f'{v1} x {v2} = {r}')
        continue
    if s == 3:
        if v1 > v2:
            r = v1
            print(f'Entre {v1} e {v2} o maior é {r}')
            continue
        elif v2 > v1:
            r = v2
            print(f'Entre {v1} e {v2} o maior é {r}')
            continue
        else:
            print(f'{v1} e {v2} são iguais')
            continue
    if s == 4:
        print('Informe os números novamente')
        v1 = float(input('Digite o valor 1: '))
        v2 = float(input('Digite o valor 2: '))
print('Programa Finalizado')
