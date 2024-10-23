#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print('+-*:' * 10)
print('{:=^40}'.format( ' TABUADA '))
print('+-*:' * 10)
n = int(input('Digite um número: '))
for c in range(1,11):
    r = n * c
    print(f'{n} * {c} = {r}')
