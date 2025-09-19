import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Extraindo os 5 países com maior GDP desse dataset

dfMaioresGDP = dfPaises.nlargest(5, "GDP ($ per capita)")
print(dfMaioresGDP['Country'])

# Plotando um gráfico em barras
plt.bar(dfMaioresGDP['Country'], dfMaioresGDP['GDP ($ per capita)'])
plt.show()