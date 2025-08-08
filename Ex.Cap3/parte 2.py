# Questão 4

nome = []
peso = []

for i in range(3):
    nome.append(input('Digite o nome da pessoa: '))
    peso.append(float(input('Digite o peso da pessoa: ')))

# Nome da pessoa mais leve:

indice_menor = peso.index(min(peso))
print(nome[indice_menor]) # Índice tem que ser inteiro

# Nome da pessoa mais pesada:

indice_maior = peso.index(max(peso))
print(nome[indice_maior])

# Questão 5

nome = []
idade = []
sexo = []

n = int(input("Quantas pessoas deseja cadastrar? "))

while n > 0:
    nome.append(input('Digite o nome da pessoa: '))
    idade.append(int(input('Digite a idade da pessoa: ')))
    sexo.append(input('Digite o sexo da pessoa: '))
    n = n - 1

# Média de idade do grupo:

media = sum(idade) / len(idade)
print(media)

qntMulheres = 0

# Quantas mulheres tem menos de 20 anos:
for i in range(len(sexo)):
    if sexo[i] == 'F' and idade[i] < 20:
        qntMulheres+=1

print(qntMulheres)
