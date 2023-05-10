import os
import pandas as pd
import plotly.express as px

# percorrer todos os arquivos da pasta base de dados (vendas)
lista_arquivos = os.listdir('Vendas')
tabela_total = pd.DataFrame()



# importar bases de dados de vendas
for arquivo in lista_arquivos:
    if 'Vendas' in arquivo:
        tabela = pd.read_csv(f'Vendas/{arquivo}')
        tabela_total = pd.concat([tabela_total, tabela])


# tratar / compilar as bases de dados
# print(tabela_total)


tabela_produtos = tabela_total.groupby('Produto').sum()[['Quantidade Vendida']]
tabela_produtos = tabela_produtos.sort_values(by='Quantidade Vendida', ascending=False)

#calc o produto que mais vendeu

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento.sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_faturamento)


# loja e cidade que mais vendeu

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)


grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()