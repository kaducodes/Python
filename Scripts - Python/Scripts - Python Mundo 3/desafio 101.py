#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL o OBRIGATÓRIO nas eleições

def voto(ano):   
    from datetime import date 
    ano_atual = date.today().year
    idade = ano_atual - ano 
    if idade < 16:
        return f'Com {idade} anos: NÃO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: OPCIONAL.'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO.'
        

#Programa principal
print('-' * 40)
a = int(input("Em que ano você nasceu? "))
print(voto(a))
