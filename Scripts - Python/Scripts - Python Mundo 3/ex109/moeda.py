def metade(valor, moeda=False):    
    if moeda:
        return f'R$ {valor :.2f}'
    else: 
        return valor / 2


def dobro(valor, moeda=False):
    if moeda:
        return f'R$ {valor :.2f}'
    else: 
        return valor * 2


def aumentar(valor, porcentagem, moeda=False):
    if moeda:
        return f'R$ {valor :.2f}'
    else: 
        return valor * (1 + porcentagem / 100)


def diminuir(valor, porcentagem, moeda=False):
    if moeda:
        return f'R$ {valor :.2f}'
    else: 
        return valor * (1 - porcentagem / 100)