# Questão 1
campeonato = ['Real Madrid', 'Barcelona','Atlético de Madrid', 'Girona', 'Real Betis']

# Mostrando apenas os 3 primeiros colocados:

print(campeonato[:3])

# Mostrando os últimos dois colocados:

print(campeonato[3:])

# Mostrando a lista dos times em ordem alfabética:

print(sorted(campeonato)) # Pode ser campeonato.sort() também

# Mostrando a posição que se encontra o Barcelona

print(f"{campeonato.index('Barcelona') + 1}° lugar") # Como inicia em 0, temos que somar 1 para achar a posição

# Questão 2

loja1 = {'iPhone 15 Pro Max', 'Samsung Galaxy S24 Ultra', 'Google Pixel 9 Pro', 'Xiaomi 14 Ultra', 'Motorola Edge 50 Pro'}
loja2 = {'Motorola Edge 50 Pro', 'Samsung Galaxy S24 Ultra', 'ASUS ROG Phone 8 Pro', 'Realme GT 6'}

# Mostrando todos elementos e depois a interseção entre os modelos das duas lojas.

print(sorted(loja1.union(loja2)))
print(sorted(loja1.intersection(loja2)))

# Questão 3

nome = input('Digite seu nome: ')
media = float(input('Digite sua média: '))
passou = media >= 50
aluno = {'nome':nome,
         'media': media,
         'passou': passou
         }

print(aluno)


