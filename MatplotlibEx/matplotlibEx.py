import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("paises.csv", delimiter=';')
df1 = pd.read_csv("space.csv", delimiter=';')

# Exercício 1:

# Filtrar países da América do Norte
paisesAmerica = df[df['Region'].str.contains('NORTHERN AMERICA')]

# Pegar Deathrate e Birthrate
DeathRate = paisesAmerica['Deathrate']
BirthRate = paisesAmerica['Birthrate']
Countries = paisesAmerica['Country'] 

# Plotando os dois gráficos no mesmo plano
plt.plot(Countries, DeathRate, 's--r', linewidth=1, markersize=10, label='Deathrate')
plt.plot(Countries, BirthRate, 'o-.b', linewidth=1, markersize=8, label='Birthrate')

# Melhorias visuais
plt.xlabel("Países")
plt.ylabel("Taxas")
plt.title("Taxa de Mortalidade e Natalidade - América do Norte")
plt.grid(True)
plt.legend()
plt.show()

# Exercício 2

spaceUSA = df1[df1['Location'].str.contains('USA')]
spaceChina = df1[df1['Location'].str.contains('China')]
empresasEspaciaisGeraisUSA = spaceUSA['Company Name']
empresasEspaciaisGeraisChina = spaceChina['Company Name']
empresasUSA, qntUSA = np.unique(empresasEspaciaisGeraisUSA, return_counts= True)
empresasChina, qntChina = np.unique(empresasEspaciaisGeraisChina, return_counts= True)

# Quantidade de empresas únicas
valores = [len(qntUSA), len(qntChina)]
labels = ['USA', 'China']

plt.bar(labels, valores)
plt.ylabel('Número de empresas espaciais únicas')
plt.title('Empresas espaciais por país')
plt.show()

# Exercício 3

missoesRoscosmos = df1[df1['Company Name'].str.contains('Roscosmos')]
missionSuccess = missoesRoscosmos[missoesRoscosmos['Status Mission'] == 'Success']
missionFailure = missoesRoscosmos[missoesRoscosmos['Status Mission'] == 'Failure']

plt.pie([len(missionSuccess), len(missionFailure)], labels = ['Missões realizadas com Sucesso', 'Missões realizadas com Falha'], autopct= '%1.1f%%')
plt.title('Missões realizadas pela empresa Roscosmos')
plt.show()





