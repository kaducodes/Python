#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#ex: Ana Maria de Souza
#primeiro=Ana último=Souza
n = str(input('Digite seu nome completo: ')).strip().capitalize()
print('Muito prazer em te conhecer!')
lista = n.split()
print('O primeiro nome é {}.'.format(lista[0]))
print('E o seu último nome é {}.'.format(lista[len(lista)-1]))

print(len(n))
print(len(lista))

