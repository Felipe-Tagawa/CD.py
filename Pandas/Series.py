import pandas as pd

# 2 Coleções:
    # Series - 1D
    # DataFrame - 2D+

# SERIES - índices + valores:

indices = ['a', 'b', 'c']
valores = [10, 20, 30]

dic = {'a':10, 'b':20, 'c':30}
dic2 = {'a':10, 'b':20, 'd':40}

series = pd.Series(index = indices, data=valores)
series2 = pd.Series(dic2)

"""" Mostrando Series
print(series)
a    1
b    2
c    3
dtype: int64
"""
# ou
"""
series = pd.Series(dic)
print(series)
"""

# Mostrar elemento específico
#print(series['a'])

# Operações entre Series - Ocorrem elemento a elemento('a' da 1 com 'a' da 2)

#print(series + series2)

#print(series - series2)

# Soma e Subtraçõa com funções do pandas

print(series.add(series2, fill_value=0)) # Fazendo soma elemento a elemento com valor padrão 0
print(series.sub(series2, fill_value=0)) # Fazendo subtração elemento a elemento com valor padrão 0

# Condicionais no Pandas

print(series[series <= 20])






