# passo a passo
# Passo 1: importar a base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")

# Passo 2: visualizar a base de dados
    # entender o que tem na base de dados
    # encontrar a cagadas da base de dados

    # colunas inúteis - informação que não te ajuda, te atrapalha!
    # tirar a coluna de CustomerID
tabela = tabela.drop(columns="CustomerID")
print(tabela)

# Passo 3: tratamento de dados - corrigir as cagadas da base de dados
    # informações no formato errado
print(tabela.info())

    # valores vazios - exluir as linhas que têm valores vazios
tabela = tabela.dropna()
# tabela = tabela.fillna() - método para preencher os valores vazios

print(tabela.info())

# Passo 4: análise inicial dos cancelamentos
print(tabela["cancelou"].value_counts()) #contando quantos clientes cancelaram e não cancelaram na coluna

print(tabela["cancelou"].value_counts(normalize=True)) #passar os valores em percentual em decimal

print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) #passar os valores em percentual

# Passo 5: análise de causas do cancelamento dos clientes
import plotly.express as px

# cria o gráfico
# for coluna in tabela.columns:
    #cria gráfico
    # grafico = px.histogram(tabela, x=coluna, color="cancelou")

    # exibe o gráfico
    # grafico.show()

# todos os clientes que ligaram mais de 4x pro call center, cancelaram
    # criar um processo interno para resolver os problemas do cliente em no máximo 2 igações
# todos os clientes que atrasaram mais de 20 dias o pagamento, cancelaram
    # criar um processo que quando bate 10 dias de atraso no pagamento, liga um alerta
# todos os clientes de contrato mensal, cancelaram
    # oferecer desconto no contrato anual/trimestral

# filtrar base de dados

# se eu resolver o call center, pra quando cai o cancelamento?
filtro = tabela["ligacoes_callcenter"]<=4
tabela = tabela[filtro]

# e o atraso?
filtro = tabela["dias_atraso"]<=20
tabela = tabela[filtro]

# e contrato mensal?
filtro = tabela["duracao_contrato"]!="Monthly"
tabela = tabela[filtro]

print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
