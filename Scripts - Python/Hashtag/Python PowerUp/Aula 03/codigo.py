# ferramenta mais usada na área de IA: scikit-learn

# Passo a passo
# Passo 0: Entender o desafio da empresa e da sua área
# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("clientes.csv")
# print(tabela)

# verificar se a base de dados tem problemas
# print(tabela.info())

# Passo 2: Preparar a base de dados para a Inteligência Artificial
# IA não trabalha com texto, pra isso temos que tratar as colunas que são object
# Label Encoder (atribuir um número para cada profissão)
from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

# profissao
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])

# mix_credito
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])

# comportamento_pagamento
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

# print(tabela.info())

# Dividir em 2:
# coluna que quer prever (y) e
# colunas vai usar para fazer a previsão (x)
# score_credito
x = tabela.drop(columns=["score_credito", "id_cliente"])
y = tabela["score_credito"]

# Dividir em 2 (Machine Learning):
# dados de treino (x_treino e y_treino) e
# dados de testes (x_teste e y_teste)
from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

# Passo 3: Criar alguns modelos de IA -> Nota de crédito: Ruim, Média ou Boa
# Modelo RandomForest -> Árvore de Decisão
from sklearn.ensemble import RandomForestClassifier #importar IA
modelo_arvoredecisao = RandomForestClassifier() #criar IA
modelo_arvoredecisao.fit(x_treino, y_treino) #treinar IA

# Modelo Neirest Neighbors (KNN) -> Vizinhos Próximos
from sklearn.neighbors import KNeighborsClassifier #importar IA
modelo_knn = KNeighborsClassifier() #criar IA
modelo_knn.fit(x_treino, y_treino) #treinar IA

# Passo 4: Escolher o melhor modelo
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

from sklearn.metrics import accuracy_score

print("A acurácia do Método Árvore de Decisão é: ")
print(accuracy_score(y_teste, previsao_arvoredecisao))
print("A acurácia do Método Vizinhos Próximos é: ")
print(accuracy_score(y_teste, previsao_knn))

# modelo_arvoredecisao é melhor para essa base de dados

# Passo 5: Usar o noso modelo para fazer novas previsões

# importar novos clientes para prever
tabela_novos_clientes = pd.read_csv("novos_clientes.csv")
print(tabela_novos_clientes)

# ajustar as colunas de texto
tabela_novos_clientes["profissao"] = codificador.fit_transform(tabela_novos_clientes["profissao"])
tabela_novos_clientes["mix_credito"] = codificador.fit_transform(tabela_novos_clientes["mix_credito"])
tabela_novos_clientes["comportamento_pagamento"] = codificador.fit_transform(tabela_novos_clientes["comportamento_pagamento"])

# fazer previsões com o modelo escolhido (modelo_arvoredecisao)
previsoes = modelo_arvoredecisao.predict(tabela_novos_clientes)

print(previsoes)