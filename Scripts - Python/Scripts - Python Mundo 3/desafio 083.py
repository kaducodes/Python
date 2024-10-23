#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() # remove o último elemento de uma lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

#abertos = []
#abertos.append('(')
#fechados = []
#fechados.append(')')
#if len(abertos) == len(fechados):
#    print('Sua expressão está certa!')
#else:
#    print('Sua expressão está errada!')
#print(len(abertos))
#print(len(fechados))
#Seu app deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#Digite a expressão: ((a+b)*c)
#Sua expressão está certa!