#Crie um pacote chamado utilidadeCeV que tenha dois módulos internos chamados moeda e dado.

#Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

#Pastas
#utilidadescev - dados
#              - moedas

from ex111.utilidadescev import moeda

p = float(input('Digite o Preço: R$ '))
moeda.resumo(p, 20, 12)

#35% de aumento
#22% de redução
#-----------------------------
#        RESUMO DO VALOR
#-----------------------------
#Preço analisado: R$
#Dobro do preço:  R$
#Metade do preço: R$
#35% de aumento:  R$
#22% de redução:  R$
#-----------------------------