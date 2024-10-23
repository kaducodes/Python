#Crie um programa que tenha uma tupla única
#com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular
#Definindo a tupla das tuplas
listagem = (
    'Guitarra' , 2200,
    'Baixo', 3000,
    'Microfone', 2000,
    'Bateria', 4000,
    'Teclado', 3000
    )
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
print('INTRUMENTO                       PREÇO')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)

