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
acima = []
cont = 0
soma_idade = 0
media = 0

while True:
    cont += 1
    perfil = {}

    perfil['nome'] = str(input("Nome: "))

    while True:
        perfil['sexo'] = str(input("Sexo [M/F]: ")).upper().strip()
        if perfil['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F")

    perfil['idade'] = int(input("Idade: "))
    soma_idade += perfil['idade']
    lista.append(perfil.copy())

    while True:
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
        if resp in 'SN':
            break
        print("ERRO! Por favor, digite apenas S ou N")
    if resp == "N":
        break

media = soma_idade / cont
for p in lista:
    if p['idade'] > media:
        acima.append(p['nome'])

print(lista)
print('-=' * 30)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {media :.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print('      ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')