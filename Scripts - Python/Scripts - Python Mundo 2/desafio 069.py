#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
print('-'*40)
print('CADASTRE UMA PESSOA')
print('-'*40)
maior = masc = fem = 0
while True:
    sexo = pergunta = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-'*40)
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    print('-' * 40)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1
    if pergunta == 'N':
        break
print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {fem} mulheres com menos de 20 anos')
