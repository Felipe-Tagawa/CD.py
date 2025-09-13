import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', delimiter = ';' )
print(ds.columns) # Mostrando a primeira linha(colunas)
print(ds.head(2)) # Mostrando as duas primeiras linhas
print(ds.tail(1)) # Mostrando a última linha

# Adicionar nova coluna no dataset
# Criar uma coluna que mostre a porcentagem da população de cada país em relação a população global

# Calculando a população total
somaPopulacao = np.sum(ds['Population'])
print(somaPopulacao)

# Calculando a porcentagem da população de cada país no mundo
populationPerc = ds['Population']/somaPopulacao
print(populationPerc)

# Adicionar a nova coluna no dataset
ds['PopulationPercent'] = populationPerc
print(ds)

# Criando uma nova versão do dataset

ds.to_csv('paises2.csv', sep=';')

# Agrupamento de Dados

# Região
group_region = ds.groupby('Region')
print(group_region.count()['Country'])
print(group_region.sum()['Country']) # Quais países são de cada região
print(group_region.sum()['Population']) # População de cada região

# Funções customizadas no Pandas

# Função que da um desconto de 10% em algo
def tenPercent(x):
    return x * .9

# Pegando a taxa de mortalidade do dataset
taxaMort = ds['Deathrate']

# Criando uma nova Series descontando 10% da taxa de mortalidade
taxaMort2 = taxaMort.apply(tenPercent)

# Criando um novo dataframe apenas com estas duas series
df2 = pd.concat([taxaMort, taxaMort2], axis = 1)
df2.columns = ['Taxa de Mortalidade', 'Taxa de Mortalidade com Desconto']
print(df2)

# Dados Ausentes

novoDataframe = ds.dropna() # Remove linhas que possuam dados ausentes
novoDataframe = ds.fillna(0) # Preencher os valores ausentes com o valor 0
