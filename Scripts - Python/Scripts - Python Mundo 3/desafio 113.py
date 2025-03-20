#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n            
    

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return f'{n:.2f}'.replace('.', ',') 


i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {i} e o Real foi {r}')



#enquanto não digitar um valor válido mostrar essas msgs:
#ERRO: por favor, digite um número inteiro válido.
#ERRO: por favor, digite um número real válido.
#se o usuário não digitar nada, o programa vai considerar 0
