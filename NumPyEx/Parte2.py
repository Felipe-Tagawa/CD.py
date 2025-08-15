import numpy as np

# Ex4:

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)

print(matriz.shape[0])
print(matriz.shape[1])

# Produto da # de linhas pela # de colunas
print(matriz.shape[0] * matriz.shape[1])

# Número ímpar de elementos:

print(np.reshape(matriz, (1,9)))
print(np.reshape(matriz, (9,1)))

# Ex5:

# Seed 10 utilizada para padrões de valores aleatórios
np.random.seed(10)
mtz = np.random.randint(0, 51, 16)

# Matriz 4 x 4 de valores aleatórios:

result = mtz.reshape(4,4)
print(result)

# Média de cada linha

mediaLinhas = np.mean(result, axis=1)
print("\n", "Média das linhas: ", mediaLinhas)

# Média de cada coluna

mediaColunas = np.mean(result, axis=0)
print("\n", "Média das colunas", mediaColunas)

# Maior valor das médias das linhas:

print("\n", mediaLinhas.max())

# Maior valor das médias das colunas

print("\n", mediaColunas.max())

# Mostrando a quantidade de aparições de cada valor na matriz

valores, contagem = np.unique(result, return_counts = True)
print("\n", valores, contagem)

# Mostrando apenas os valores que aparecem 2 vezes

valoresDuplicados = valores[contagem == 2]

print("\n valores duplicados: ", valoresDuplicados)