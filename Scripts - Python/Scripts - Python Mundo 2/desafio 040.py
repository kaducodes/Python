#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('=' * 28)
print('Programa - Média e Aprovação')
print('=' * 28)
n1 = float(input('Nota - Unidade I: '))
n2 = float(input('Nota - Unidade II: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.2f}')
if m >= 7:
    print('APROVADO')
elif m >= 5 and m < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
