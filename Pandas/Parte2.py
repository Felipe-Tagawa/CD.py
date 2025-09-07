import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1,50,[5,4])
    )

print(df)

# Exercício 6

print(f"A média dos elementos da coluna 'X' que são menores que 30: {df.loc[df['X'] < 30, 'X'].mean()}")

# Exercício 7

print(f"A média dos elementos da linha 'D' usando loc: {df.loc['D'].mean()}")

print(f"A média dos elementos da linha 'E' usando iloc: {df.iloc[4, :].mean()}")

# Exercício 8

set = df.loc[['A','C','E'], ['X', 'Y']]
print("Soma das colunas:")
print(set.sum(axis=0))
print("Soma das linhas:")
print(set.sum(axis=1))

