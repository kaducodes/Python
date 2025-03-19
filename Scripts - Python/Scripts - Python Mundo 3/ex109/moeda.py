def metade(valor, formatado=False):    
    if formatado:
        return f'R$ {valor :.2f}'
    else: 
        return valor / 2


def dobro(valor, formatado=False):
    if formatado:
        return f'R$ {valor :.2f}'
    else: 
        return valor * 2


def aumentar(valor, porcentagem, formatado=False):
    if formatado:
        return f'R$ {valor :.2f}'
    else: 
        return valor * (1 + porcentagem / 100)


def diminuir(valor, porcentagem, formatado=False):
    if formatado:
        return f'R$ {valor :.2f}'
    else: 
        return valor * (1 - porcentagem / 100)