#Dicionários
#Declaração
#dados = dict()
dados = {'nome':'Kadu', 'idade':39}
print(dados['nome'])
#Adicionar Elementos
dados['sexo'] = 'M'
print(dados)
#Deletar elementos
del dados['idade']

filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values())
print(filme.keys())
print(filme.items())

#Laço para iterar dicionário, semelhante ao enumarate nas tuplas e listas
for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Kadu', 'sexo': 'M', 'idade': 39}
for k, v in pessoas.items():
    print(f'{k} = {v}')

#Criando dicionário dentro de lista (forma mais comum em sistemas)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])

estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
