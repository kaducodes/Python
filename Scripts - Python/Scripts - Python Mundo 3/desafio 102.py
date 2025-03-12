#Crie um programa que tenha uma função chamada fatorial() que receba 2 parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

#fatorial (3, show=False)
#6
#fatorial (3, show=True)
# 3 x 2 = 6

#help(fatorial)
#documenta a função

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    : parâmetro num: O número a ser calculado
    : parâmetro show: (opcional) Mostrar ou não a conta
    : return: O valor do Fatorial de um número
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)