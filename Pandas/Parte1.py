import pandas as pd

# Exercício 1

# Criando Series com índices : valores
indices = ['Java', 'C', 'Python']
valores = [16.25, 16.04, 9.85]

# Criando Series com dicionário:
dictionary = {'C': 16.21, 'Python': 12.12, 'Java': 11.68}

seriesAno1 = pd.Series(index = indices, data = valores)
seriesAno2 = pd.Series(dictionary)

# Exercício 2

porcentAno1 = seriesAno1.sum()
print(f"A porcentagem das 3 linguagens no ano 1 foi de {porcentAno1:.2f}%")

porcentAno2 = seriesAno2.sum()
print(f"A porcentagem das 3 linguagens no ano 2 foi de {porcentAno2:.2f}%")

# Exercício 3

print(seriesAno2.sub(seriesAno1).round(2).astype(str) + "%")

# Exercício 4

raise_ = seriesAno2.sub(seriesAno1).round(2)

print(raise_[raise_ > 0].astype(str) + "%")

# Exercício 5

porcentRaise = (3 * seriesAno2.sub(seriesAno1).round(2)).nlargest(1).round(2) # 3x pois 1x é o sub inicial, mais 2x de 2 anos
print(porcentRaise.astype(str) + "%")


