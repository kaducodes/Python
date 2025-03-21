#Exception: 
#NameError, ValueError, ZeroDivisionError, TypeError, IndexError, KeyError, EOFError, KeyboardInterrupt, OSError, MemoryError, ConnectionError, RuntimeError

#try:
#   operação
#except:
#   falhou

#Tratamento de erro:
#else e finally são opcionais para tratamento dos erros
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultador é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
