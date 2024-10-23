
print('Digite os dados do espaço a ser utilizado (em metros):')
c = float(input('comprimento: '))

print('Digite os dados da placa escolhida (em metros):')
lp = float(input('largura da placa: '))
ep = float(input('espaçamento entre placas: '))

s = int(input('''Terá espaçamentos:
[1] no começo e no final
[2] apenas no começo ou no final
[3] não terá
'''))

if s == 1:
    e1 = float(input('espaçamento inicial: '))
    e2 = float(input('espaçamento final: '))
    qtd = (c - e1 - e2) // (lp + ep)
    resto = (c - e1 - e2) % (lp + ep)
    print(f'você irá precisar de {qtd:.0f} placas de {lp:.2f}m largura')
    if resto == 0:
        print()
    else:
        print(f'mas sobrou {resto:.2f}m no seu espaço.')
elif s == 2:
    e = float(input('espaçamento: '))
    qtd = (c - e) // (lp + ep)
    resto = (c - e) % (lp + ep)
    print(f'você irá precisar de {qtd:.0f} placas de {lp:.2f}m largura')
    if resto == 0:
        print()
    else:
        print(f'mas sobrou {resto:.2f}m no seu espaço.')
elif s == 3:
    qtd = c // (lp + ep)
    resto = c % (lp + ep)
    print(f'você irá precisar de {qtd:.0f} placas de {lp:.2f}m largura')
    if resto == 0:
        print()
    else:
        print(f'mas sobrou {resto:.2f}m no seu espaço.')

