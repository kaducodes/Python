#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
dividir = nome.split()
junto =''.join(dividir)
print(f'Seu nome ao todo tem {len(junto)} letras')
letras = len(nome) - nome.count(' ')
print(f'Sério!! seu nome ao todo tem {letras} letras... acredite!')
print(f'Seu primeiro nome é {dividir[0]} e ele tem {len(dividir[0])} letras')
