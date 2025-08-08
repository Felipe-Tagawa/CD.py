# Coleção com relação key:value
pessoa = {'nome': 'Goku',
          'idade': 43,
          'sexo': 'masculino'
          }
print(pessoa)

# Adição

pessoa['raca'] = 'sayajin'
pessoa['familia'] = ['Gohan', 'Goten', 'Chichi', 'Pan']

# Update

pessoa['idade'] = 45

# Delete
del pessoa['sexo']

print(pessoa)

# Acessando a Chichi

print(pessoa['familia'][-2])

