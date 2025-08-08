# Listas - Coleção totalmente mutável

lista = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# Mostrando os elementos da lista

print(lista)

# Inserindo elementos no final da lista

lista.append('Bulma')

# Inserindo elementos em um lugar específico

lista.insert(1, 'Kuririn')
print(lista)

# Alterando elementos na lista

lista[0] = 'Piccolo'
print(lista)

# Excluindo elementos

del lista[0] # Remoção pelo índice
lista.remove('Bulma')
print(lista)



