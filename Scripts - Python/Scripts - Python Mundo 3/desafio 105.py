#Crie um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings da função

#resp = notas(5.5, 9.5, 10, 6.5, sit=True)

#{'total': 4, 'maior': 10, 'menor': 5.5, 'média': 7.875, 'situação: 'BOA'}

cont = 1
maior = menor = soma = media = 0

def notas(*n, sit=False):
    """
    notas(*n, sit=False)
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = {}
    r['total'] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r["situação"] = 'BOA'
        elif r['media'] >= 5:
            r["situação"] = 'RAZOÁVEL'
        else:
            r["situação"] = 'RUIM'

    return r


#Programa principal
print(notas(9, 10, 9, 10, sit=True))
help(notas)