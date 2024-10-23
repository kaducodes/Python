n = str(input('Qual o seu nome: ')).strip()
n2 = n.upper()
print(f'Bom dia, {n.capitalize()}!')
if n2 in 'ANNA LIDIA KADU CARLOS EDUARDO VICTOR':
    print(f'Que nome lindão, {n.capitalize()}')
elif n2 == 'MILA' or n2 == 'SEGUNDO' or n2 == 'CAETANO':
    print(f'Seu nome até que é legal, {n.capitalize()}...')
else:
    print(f'Seu nome é muito normal, {n.capitalize()}... Mas de boa!')


