#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

#aceita tanto . quanto ,
#ERRO: "barato é um preço inválido!
#ERRO: "" é um preço inválido!

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o Preço: R$ ')
moeda.resumo(p, 35, 22)

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