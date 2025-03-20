#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

while True:
    print('-' * 60)
    print('MENU PRINCIPAL'.center(60))
    print('-' * 60)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-' * 60)
    opc = int(input('Sua Opção: '))

    if opc == 1:
        print('-' * 60)
        print('PESSOAS CADASTRADAS'.center(60))
        print('-' * 60)

    elif opc == 2:
        print('-' * 60)
        print('NOVO CADASTRO'.center(60))
        print('-' * 60)
        nome = str(input('Nome: '))
        while True:
            try:
                idade = int(input('Idade: '))
            except ValueError:
                print('ERRO: Por favor, digite um número inteiro válido')
            else:
                print(f'Novo registro de {nome} adicionado')
                break
        

    elif opc == 3:
        print('Saindo do sistema... Até logo!'.center(60))
        break
    
    else:
        print('ERRO: Digite uma opção válida!')
