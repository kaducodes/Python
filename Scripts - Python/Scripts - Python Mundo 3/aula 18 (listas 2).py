dados = []
dados.append('Pedro')
dados.append('25')
print(dados) #['Pedro', '25']
pessoas = [['Maria', 19], ['Joao', 32]]
pessoas.append(dados[:]) #[:] representa uma cópia
print(pessoas) #[['Maria', 19], ['Joao', 32], ['Pedro', '25']]
print(pessoas[2][0]) #Pedro
print(pessoas[0]) #['Maria', 19]
print('-='*30)
galera = [['Kadu', 38], ['Anna', 29], ['Victor', 2]]
dado = []
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # importante fazer cópia de dados que senão o print mostra com o clear()
    dado.clear()
print(galera)
maior = menor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade')