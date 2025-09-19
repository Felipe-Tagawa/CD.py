import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Gráfico de dispersão(Scatter Plot)

dfPaises = pd.read_csv('paises.csv', delimiter=';')
print(dfPaises.columns)

# Extraindo os 6 maiores países em área do mundo

dfMaioresPaises = dfPaises.nlargest(6, 'Area (sq. mi.)')
print(dfMaioresPaises['Country'])

# Traçar um Sccater Plot que ilustre o GDP per capita destes países

plt.scatter(dfMaioresPaises['Country'], dfMaioresPaises['GDP ($ per capita)'], s = 500)
plt.show()