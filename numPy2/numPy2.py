import numpy as np
# Slicing em Numpy Array

# Criando uma matriz:

mtz = np.arange(1,10,1).reshape(3,3)
print(mtz)

# Extraindo apenas uma linha (terceira linha)

print(mtz[2])

# Extraindo apenas uma coluna (segunda e terceira colunas) - primeiro : --> todas as linhas

print(mtz[:,1:])

# CONDICIONAIS NO NUMPY ARRAY

print(mtz>5)
print(mtz[mtz>5]) # Mostra quais são os valores maiores do que 5 dentro da matriz
print(mtz[mtz%2==0])

# Tratamento de textos no Numpy (subpacote char)

jogadores = np.array(['Gouenji', 'Endo', 'Kidou', 'Kazemaru', 'Fubuki', 'Kageyama'])
print(jogadores)
print(np.char.find(jogadores, 'Ka')>=0)
print(jogadores[np.char.find(jogadores, 'Ka')>=0]) # -1 simboliza que não aquele padrão

jogadores  = np.char.upper(jogadores) # Padronização para buscas independente de Upper Case
print(jogadores[np.char.find(jogadores, 'KA')>=0])

