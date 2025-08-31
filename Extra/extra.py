import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype='str',
                encoding= 'utf-8')

# Questão 1

data = ds[1:]

# Mostrar as 4 primeiras colunas
print(data[0:,:4])

# Questão 2

print()

region = data[:,1]

print(f"{len(np.unique(region))} regiões diferentes")
print()
print(np.unique(region))

# Questão 3

print()
alfabetizacao = data[:, 9].astype(float)
# Não esquecer do astype
print(f"Média da alfabetização: {np.mean(alfabetizacao):.2f} %")

# Questão 4

print()
paisesNorte = data[:, 1]
print(f"{len(paisesNorte[np.char.find(paisesNorte, 'NORTHERN AMERICA') >= 0])} países são da América do Norte!")

# Questão 5

print()

paisesCaribe = data[:, 1]
renda = data[:, 8].astype(float)
boolRendaPerCapita = np.char.find(paisesCaribe, 'LATIN AMER. & CARIB') >= 0
rendaperCapitaCaribe = renda[boolRendaPerCapita]
maxIndex = np.argmax(rendaperCapitaCaribe)
paisesFiltrados = data[boolRendaPerCapita, 0]

print(f"País com maior renda: {paisesFiltrados[maxIndex]}")
print(f"Maior Renda per Capita de LATIN AMER. & CARIB : {rendaperCapitaCaribe[maxIndex]:.2f}")
