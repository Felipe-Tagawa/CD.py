import numpy as np
ds = np.loadtxt('space.csv',
                delimiter= ';', # Tipo de delimitador
                dtype=str, # Tipo de dados
                encoding='utf-8') # esse dataset especificamente pede esse encoding

# Colunas do dataset

print(ds[0, :])

# Calculando a média de uma missão espacial
# Slicing para extrair a coluna custo (Cost)

dsCost = ds[1:, 6] # 1 pra frente pra evitar a coluna 'Cost' - linha 0
# Transformando os valores em float
dsCost = dsCost.astype(float)

print(dsCost)

# Calculando a média
print(dsCost.mean())
