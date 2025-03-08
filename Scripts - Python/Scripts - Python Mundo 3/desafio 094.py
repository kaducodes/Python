#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres
#D) Uma lista com todas as pessoas com idade acima da média

#Nome:
#Sexo [M/F]: 
#Idade:
#Quer continuar? [S/N]

#- O grupo tem x pessoas.
#- A média de idade é de x anos.
#- As mulheres cadastradas foram: 
#- Lista das pessoas que estão acima da média: 

lista = []
fem = []
acima = []
cont = 0
idade = 0
media = 0

while True:
    cont += 1
    perfil = {}
    perfil['nome'] = str(input("Nome: "))
    perfil['sexo'] = str(input("Sexo [M/F]: ")).upper().strip()
    if perfil['sexo'] == "F":
        fem.append(perfil['nome'])
    perfil['idade'] = int(input("Idade: "))
    idade += perfil['idade']
    lista.append(perfil.copy())

    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if resp == "N":
        break

media = idade / cont
for pessoa in lista:
    if pessoa['idade'] > media:
        acima.append(pessoa['nome'])

print(lista)
print('-=' * 30)
print(f'   - O grupo tem {cont} pessoas.')
print(f'   - A média de idade é de {media :.2f} anos.')
print(f'   - As mulheres cadastradas foram: {fem}')
print(f'   - Lista das pessoas que estão acima da média: {acima}')