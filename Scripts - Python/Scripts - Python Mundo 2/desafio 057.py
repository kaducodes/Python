#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado pela a digitação novamente até ter um valor correto.
s = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, informe o seu sexo [M/F]: ')).strip().upper()[0]
print(f'O Sexo {s} registrado com sucesso!')