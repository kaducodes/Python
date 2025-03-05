#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#considerar aposentadoria: 35 anos de contribuição

#Nome: 
#Ano de Nascimento: 
#Carteira de Trabalho (0 se não tem):
#Ano de Contratação:
#Salário: R$ 

#{k} tem o valor {v}

from datetime import datetime

ficha = {}

ficha['nome'] = str(input("Nome: "))
ano_de_nascimento = int(input("Ano de Nascimento: "))
ano_atual = datetime.now().year
ficha['idade'] = ano_atual - ano_de_nascimento
ficha['ctps'] = int(input("Carteira de Trabalho (0 se não tem): "))

if ficha['ctps'] != 0:
    ficha['contratação'] = int(input("Ano de Contratação: "))
    ficha['salario'] = float(input("Salário: R$ "))
    ficha['aposentadoria'] = ano_atual - ficha['contratação']
    if ficha['aposentadoria'] >= 35:
        print("Parabéns! Você pode se aposentar")
    else:
        print(f"  - Faltam {35 - ficha['aposentadoria']} anos para se aposentar")
        print(f"  - Vai se aposentar com {ficha['idade'] + 35 - ficha['aposentadoria']} anos")

print('-=' * 30)
for k, v in ficha.items():
    print(f'  - {k} tem o valor {v}')


