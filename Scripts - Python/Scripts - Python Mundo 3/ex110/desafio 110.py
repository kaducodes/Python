#Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from ex110 import moeda

p = float(input('Digite o Preço: R$ '))
moeda.resumo(p, 80, 35)
#80% de aumento
#35% de redução
#-----------------------------
#        RESUMO DO VALOR
#-----------------------------
#Preço analisado: R$
#Dobro do preço:  R$