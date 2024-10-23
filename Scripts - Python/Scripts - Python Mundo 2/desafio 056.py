#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
qtdmulheres = 0
for c in range (1,5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        qtdmulheres += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho.capitalize()}')
print(f'O grupo tem {qtdmulheres} Mulheres com menos de 20 anos.')
