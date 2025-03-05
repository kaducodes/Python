#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

#Nome: 
#Média de {Nome}: 
#Nome é igual a {nome}
#Média é igual a {media}
#Situação é igual a {aprovado ou reprovado}

aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'

print('-=' * 30)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
