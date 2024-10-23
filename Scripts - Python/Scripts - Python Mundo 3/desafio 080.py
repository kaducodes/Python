#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
#Digite um valor:
#Adicionado ao final da lista...
#Adicionado na posição 0 da lista...
#Os valores digitados em ordem foram []
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Adicionado ao final da lista...')
    elif n > lista[len(lista)-1]: #lista[-1] também pega o último elemento da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista}')


# A quem interessar, bisect.insort(lista, n) já insere n na lista de forma ordenada:
# import bisect
# numbers = []
# for i in range(5):
#     n = int(input('Type a number: '))
#     bisect.insort(numbers, n)
#     print(f'Number {n} included in position {numbers.index(n)}')
# print(f'Numbers typed: numbers')