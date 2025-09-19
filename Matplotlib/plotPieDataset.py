import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfNoCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]

# Extraindo quantos países não tem costa
qtNoCoast = len(dfNoCoast)
qtCoast = len(dfPaises) - qtNoCoast

# Plotando o gráfico em pizza
plt.pie([qtNoCoast, qtCoast], labels=['Paises sem costa', 'Paises com costa'], autopct='%1.1f%%')
plt.show()

