#funções em todas as linguagens de programação descrevem rotinas do sistema. Cria funções personalizadas pelo programador
#funções que já vem no python:
#print()
#input()
#len()
#int()
#float() ...

#É interessante para a identação do código separar as funções do programa principal com 2 linhas

def mostraLinha():
    print('-' * 30)


mostraLinha()
print("     CURSO EM VÍDEO     ")
mostraLinha()
print("     APRENDA PYTHON     ")
mostraLinha()
print("     GUSTAVO GUANABARA    ")
mostraLinha()

#Função com parâmetro:
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem("     CURSO EM VÍDEO     ")
mensagem("     APRENDA PYTHON     ")
mensagem("     GUSTAVO GUANABARA    ")

#Exemplo de programa com a quantidade de parâmetros definidos
def soma(a, b):
    s = a + b
    print(s)


#programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

#Empacotamento
mostraLinha()
def contador(* num):
    tan = len(num)
    print(f'Recebi os números {num} que são {tan} números')


contador(5, 2)
contador(2, 9, 4)
mostraLinha()

#Não precisa empacotar quando o seu parâmetro é uma lista
mostraLinha()
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
mostraLinha()
