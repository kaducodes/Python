#Crie um programa que tenha uma função chamada ficha(), que receba 2 parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

#Nome do Jogador:
#Total de Gols:

#O jogador <desconhecido> fez 0 gol(s) no campeonato

def ficha(nome='<desconhecido>', gols=0):
    """
    -> Mostra ficha do jogador
    : parâmetro nome: nome do jogador
    : parâmetro gols: quantidade de gols do jogador
    : return a Ficha do jogador
    """

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#Programa principal
n = str(input('Nome do Jogador: '))
g = int(input('Total de Gols: '))
print(ficha(n, g))
help(ficha)
