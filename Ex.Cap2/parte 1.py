print('Escreva seu nome aqui: ')
nome = input()

# Nome com todas as letras maiúsculas:
print(nome.upper())

# Nome com todas as letras minúsuculas:
print(nome.lower())

# # de letras no Nome:
partes = nome.split()
if len(partes) > 1:
    numEspacos = len(partes) - 1
    print(len(nome) - numEspacos) # Remover os espaços da contagem
else:
    print(len(nome))

# Trocar o Último Nome para 'do Inatel':
if len(partes) > 1:
    partes[-1] = "do Inatel"
elif len(partes) == 1:
    partes.append("do Inatel") # Adiciona 'do Inatel' se houver um nome apenas
else:
    print("Nome sem partes!") # Caso em que o usuário simplesmente aperta o enter
nomeNovo = ' '.join(partes)
print(nomeNovo)

# Tabuada de um número escolhido pelo usuário dentro de um intervalo escolhido por ele:

print("Escreva um número para saber a tabuada: ")
tabuada = int(input())
print("Agora escreva o primeiro valor do intervalo que quer visualizar a tabuada deste valor: ")
intervalo1 = int(input())
print("Agora escreva o segundo valor do intervalo que quer visualizar a tabuada deste valor: ")
intervalo2 = int(input())
for i in range(intervalo1, intervalo2 + 1):
    print(f"{tabuada} * {i} = {tabuada * i}")

# Sexo do Usuário:

while True:
    print("Por favor, insira seu sexo: ")
    sexo = input()
    if sexo == "M":
        print('Homem')
        break
    elif sexo == "F":
        print('Mulher')
        break
    else:
        continue # Continua o while até que um valor válido seja escrito



