# Tupla - simples, seguras(sem alteração) e acesso de elementos(arquivos de configuração)

tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

#Mostrando elementos
print(tupla)

#Alterando elementos
# tupla[0] = 'Bulma' # Tuplas são coleções imutáveis
# print(tupla)

# Slicing de Elementos
print(tupla[1:3]) # Vegeta e Trunks (1 - inclusive e 3 - exclusive(não aparece))

print(tupla[2:]) # Trunks e Gohan
print(tupla[:2]) # Goku e Vegeta

print(tupla[-2]) # Trunks com índice negativo

# Funções Pré-prontas Python

print(len(tupla)) # Número de elementos da tupla
print(max(tupla))
print(min(tupla))

