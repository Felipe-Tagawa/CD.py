# Coleção NÃO ORDENADA e que NÃO ADMITE ELEMENTOS DUPLICADOS
nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Trunks', 'Goku'}

# Mostrando elementos

print(nomes)

# Adicionar elementos

nomes.add('Bulma')
nomes.add('Goku') # Não deixa adicionar
print(nomes)

# Remover elementos (não há como remover elementos por índice)

nomes.remove('Trunks')
print(nomes)

# Não permite atualizações sem ser remoção -> inserção

# Tipos dos dados

print(type(nomes))
