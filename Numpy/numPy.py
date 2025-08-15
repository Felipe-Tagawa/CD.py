import math

import numpy as np

# Criando Numpy Arrays (ndarrays)

# Elementos sempre do mesmo tipo(otimização)

array = np.array([10,20,30])

print(array)
print(type(array))

mtz = np.array([[10,20,30], [40,50,60]])
print(mtz)

print(mtz.ndim)

# Funções pra estruturas numpy arrays

# Array 1D de 1s
arr = np.ones(10)
print(arr)

# Array 2D de 0s com Reshape
mtz = np.zeros(10).reshape(5,2)
print(mtz)

# Array 2D sem Reshape

mtz = np.zeros([5,2])
print(mtz)

# Arange - Criação automática de um vetor (valor inicial(inclusive), valor final(exclusive), de valor em valor)

arr = np.arange(10, 101, 10)
print(arr)

# Menor valor

print(arr.min())

# Maior valor

print(arr.max())

# Média dos valores

print(arr.mean())

# Índice do maior valor

print(arr.argmax())

# Índice do menor valor

print(arr.argmin())

# Operações com Numpy Array

arr = np.arange(0, 9, 1)
arr2 = np.arange(9, 0, -1)

print(arr)
print(arr2)

print(arr + arr2)

# Concaternar numpy arrays

print(np.concatenate([arr, arr2]))

# Operações com matrizes

mtz = np.array([50, 10, 100, 60, 25, 100, 75, 80, 100]).reshape(3,3)
print(mtz)

print(mtz.sum(axis=1)) # Soma das linhas
print(mtz.sum(axis=0)) # Soma das colunas
print(mtz.sum(axis=0)[2]) # Soma dos valores de internet

# Broadcasting

print(mtz/10)

# Semente Aleatória

np.random.seed(10) # Gera valores aleatórios iguais
print(np.random.randint(1, 101, 10)) # 10 números aleatórios de 1 a 100

# Elementos únicos (não duplicados)

arr = np.random.randint(1, 10, 10)
print(arr)
# return_counts - retorna a quantidade que cada valor repete
print(np.unique(arr, return_counts=True))




