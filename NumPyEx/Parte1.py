import numpy as np

# Ex1:

array1 = np.ones(8)
print(array1)
array2 = np.random.randint(0, 10,8)
print(array2)

# Soma dos arrays:
arraySoma = array1 + array2
print(arraySoma)

print(arraySoma.sum())

# Mais linhas do que colunas
if np.sum(arraySoma) >= 40:
    arraySomaLinhas = np.array(arraySoma).reshape(4,2)
    print(arraySomaLinhas)

# Mais colunas do que linhas
else:
    arraySomaColunas = np.array(arraySoma).reshape(2,4)
    print(arraySomaColunas)

# Ex2:

arrPares = np.arange(0, 52, 2)
print(arrPares)

arrPares2 = np.arange(100, 49, -2)
print(arrPares2)

# Concatenando os dois numpy arrays:
concatArr = np.concatenate((arrPares, arrPares2))
print(concatArr)

# Mostrando os valores ordenados:
sorted_arr = np.sort(concatArr)
print(sorted_arr)

# Ex3 - campo minado:

campoMinado = np.zeros([2,2])
print(campoMinado)

# Adicionado um valor '1' em um lugar aleatório da matriz

linha = np.random.randint(0,2)
coluna = np.random.randint(0,2)
campoMinado[linha,coluna] = 1
print(campoMinado)

numTentativas = 0
posicoes = [(0,0), (0,1), (1,0), (1,1)]

while True:
    resposta = int(input("Digite um valor de 0 a 3: "))
    numTentativas = numTentativas + 1
    linha, coluna = posicoes[resposta]
    if campoMinado[linha,coluna] == 1:
        print("Game Over! :( Try Again!")
        break
    else:
        if numTentativas < 3:
            continue
        else:
            print("Congratulations! You beat the game! :)")
            break

