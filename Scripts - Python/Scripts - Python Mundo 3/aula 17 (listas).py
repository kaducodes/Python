#LISTAS[]
#Os valores das listas são mutáveis, você pode mudar e adicionar itens.
#adicionar -> .append()
#adicionar entre elementos -> .insert()
#apagar elementos -> del ou .pop() ou .remove()
#valores = [8,2,5,4,9,3,0]
#valores = list(range(4,8))
    #4,9,3,0
#valores.sort()
    #0,3,4,9
#valores.sort(reverse=True)
    #9,4,3,0
#len(valores)
    #7
#Laços com Listas:
#num = [2,5,9,1]
#num[2] = 3

#métodos para adicionar:
#num.append(7) #método que adiciona no final
#num.sort(reverse=True)
#num.insert(2, 2) #método que adiciona em posição escolhida
#métodos de eliminação:
#del num[3]
#num.pop(0) #método que elimina o último elemento, a não ser que você passe como parâmetro o índice que você deseja eliminar
#num.remove(2) #método que elimina a primeira ocorrência do número passado como parãmetro
#maneira de evitar um erro da linguagem:
#if 4 in num:
#    num.remove(4)
#else:
#    print('Não achei o número 4')

#print(num)
#print(f'Essa lista tem {len(num)} elementos')

# todos esses métodos eliminam o valor e refaz todos os índices

#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#o enumarate pega tanto a chave quanto os valores

#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei {v}!')
#print('Cheguei ao final da lista')

#criar uma estrutura ordenada de forma crescente
#criar 5 elementos
#valores.sort() #método que ordena todos os valores crescente
#valores.sort(reverse=True) #método que ordena todos os valores em ordem descrescente
#len(valores) #método que diz quantos valores tem em uma lista
#for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')))


#criar uma cópia de a dentro de b e pode mudar b. se não colocar o [:] elas vão estar ligadas e tudo que muda em uma, muda em outra
#a = [2,3,4,7]
#b = a[:]
#b[2] = 8
#print(f'Lista A: {a}')
#print(f'Lista B: {b}')
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
