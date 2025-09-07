import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1,50,[5,4])
    )

'''
print(df)

    W   X   Y   Z
A  10  37  16   1
B  29  26  30  49
C  30   9  10   1
D  43  41  37  17
E  37  48  12  25

'''

# Dados da tripulação
data = {
    "Nome": ["Luffy", "Zoro", "Sanji", "Nami", "Usopp", "Chopper", "Robin", "Franky", "Brook", "Jinbe"],
    "Função": ["Capitão", "Vice-Capitão", "Cozinheiro", "Navegadora", "Atirador", "Médico", "Arqueóloga", "Carpinteiro", "Músico", "Timoneiro"],
    "Recompensa (em Berries)": [3000000000, 1111000000, 1032000000, 366000000, 500000000, 1000000, 930000000, 394000000, 383000000, 1100000000],
    "Origem": ["East Blue", "East Blue", "North Blue", "East Blue", "East Blue", "Drum Island", "Ohara", "Water 7", "West Blue", "Fishman Island"]
}
 
# Criando DataFrame
dfO = pd.DataFrame(data)
print(dfO)

# Fazendo Slicing com iloc (padrão numPy - índices numéricos)

print(df.iloc[0:2,:])

# Fazendo o mesmo Slicing com loc

print(df.loc[['A','B'], ['W','X','Y','Z']])

 
