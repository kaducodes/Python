#Faça um programa que tenha uma função chamada contador() que receba 3 parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar 3 contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep

def linhas():
    print('-=' * 30)

def contador(inicio, fim, passo):

    #Verificações
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    linhas()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
    linhas()


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input("Início: "))
fim =    int(input("Fim:    "))
passo =  int(input("Passo:  "))
contador(inicio, fim, passo)
