import numpy as np

ds = np.loadtxt('shopping_trends.csv',
                delimiter=',',
                dtype='str',
                encoding='utf-8')

#print(ds)

data = ds[1:] # Pegar somente as linhas abaixo dos títulos(1° linha)

# Exercício 1 - Mostre qual a média de idade dos homens presentes nesse dataset

# --------------------------------------------------------------------------------------- #

genero = data[:, 2] # Coluna de gênero
idade = data[:, 1].astype(int) # Coluna de idade

filtroHomem = np.char.find(genero, "Male") >= 0 # Filtro para apenas homens
valorGeral = idade[filtroHomem] # Idades dos homens

print(f"A média de idade dos homens é igual a {valorGeral.mean():.2f} anos!")

# --------------------------------------------------------------------------------------- #

# Exercício 2 - Mostre quantos clientes gastaram mais do que a média de gastos das compras deste dataset

# --------------------------------------------------------------------------------------- #

gastos = data[:, 5].astype(int) # Coluna dos gastos do tipo int
mediaGastos = gastos.mean() # Média dos gastos dos clientes
print(f"A média de gastos dos clientes foi de USD {mediaGastos:.2f}!")

print(f"A quantidade de clientes que gastaram mais do que a média foi de {len(gastos[gastos>mediaGastos])}!")

# --------------------------------------------------------------------------------------- #

# Exercício 3 - Mostre qual é a porcentagem de vendas do item menos vendido da loja

# --------------------------------------------------------------------------------------- #

itemComprado = data[:, 3] # Coluna dos itens
item, quantidade = np.unique(itemComprado, return_counts=True)
qntMenor = np.argmin(quantidade)

print(f"A menor quantidade de item vendido foi de {quantidade[qntMenor]} itens!")
print(f"A porcentagem do item menos vendido da loja foi de {(quantidade[qntMenor] / len(itemComprado)) * 100:.2f}%!")

# --------------------------------------------------------------------------------------- #

# Exercício 4 - Mostre qual a porcentagem de vendas que tiveram algum tipo de desconto

# --------------------------------------------------------------------------------------- #

descontos = np.char.rstrip(data[:, 13]) # Usar o strip pra evitar problemas com espaços indevidos
boolTeveDesconto = np.char.find(descontos, "Yes") >= 0
print(f"A porcentagem de vendas com desconto foi de {(len(descontos[boolTeveDesconto]) / len(descontos)) * 100}%!")

# --------------------------------------------------------------------------------------- #

# Exercício 5 - Mostre qual a cor de roupa mais popular no verão segundo este dataset

# --------------------------------------------------------------------------------------- #

season = data[:, 9]
apenasVerao = np.char.find(season, "Summer") >= 0 # Filtro para apenas verão
cor = data[:, 8][apenasVerao] # Cores apenas do verão
coresRepetidas, qntRepetida = np.unique(cor, return_counts=True) # Quantidade de repetições
corMaisRepetida = np.argmax(qntRepetida) # Índice da cor mais repetida do verão
print(f"A cor mais popular do verão foi {coresRepetidas[corMaisRepetida]}!")

# --------------------------------------------------------------------------------------- #




