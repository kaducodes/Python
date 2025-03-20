def moeda (valor):
    return f'R$ {valor :.2f}'.replace('.', ',')


def metade(valor):
    return f'{valor / 2}'.replace('.', ',')


def dobro(valor):
    return f'{valor * 2}'.replace('.', ',')


def aumentar(valor, porcentagem):
    return f'{valor * (1 + porcentagem / 100)}'.replace('.', ',')


def diminuir(valor, porcentagem):
    return f'{valor * (1 - porcentagem / 100)}'.replace('.', ',')