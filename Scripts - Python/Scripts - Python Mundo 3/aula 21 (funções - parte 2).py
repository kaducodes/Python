#Interative Help
    #help(print)
    #print(input.__doc__)

#docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :parâmetro i: início da contagem
    :parâmetro f: fim da contagem
    :parâmetro p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)

#Argumentos opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c 
    print(f'A soma vale {s}')


somar(3,2,5)
somar(8,4)
somar(3)
somar()

#Escopo de variáveis
def funcao(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a local vale {a}')
    print(f'a local vale {b}')
    print(f'a local vale {c}')

a = 5
print(f'a global vale {a}')
funcao(a)
print(f'a global agora vale {a}')

#Retorno de resultados
def somar(a=0, b=0, c=0):
    s = a + b + c 
    return s


r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar(3)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

#Exemplo com fatorial
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(fatorial(n))