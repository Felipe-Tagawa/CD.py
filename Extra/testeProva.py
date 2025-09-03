import numpy as np

# Importando o csv:
ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')

# Primeira linha pra frente
data = ds[1:]

# Quero mostrar qual o nome do país que tem a menor taxa demográfica em Western Europe

# Coluna de países:

paises = data[:, 0]

# Coluna de região:

regiao = np.char.rstrip(data[:, 1])

# Coluna de densidade demográfica:

densidade = data[:, 4].astype(float)

boolPaisesEurope = regiao == "WESTERN EUROPE"

print(boolPaisesEurope)

Density = densidade[boolPaisesEurope]
print(Density)
minIndex = np.argmin(Density)

print(minIndex)
print(f"O menor valor de densidade populacional foi de : {Density[minIndex]}")

filtroPais = data[boolPaisesEurope, 0]
print(filtroPais[minIndex])

# Fazer a média dos valores da coluna de densidade, mas apenas se WESTERN EUROPE

print(np.mean(Density))


