# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta.
# Digite um valor para [0, 0]:
# Digite um valor para [0, 1]:
# Digite um valor para [0, 2]:
# Digite um valor para [1, 0]:
# Digite um valor para [1, 1]:
# Digite um valor para [1, 2]:
# Digite um valor para [2, 0]:
# Digite um valor para [2, 1]:
# Digite um valor para [2, 2]:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()