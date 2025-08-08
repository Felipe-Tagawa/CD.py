import math
# Exercício da passagem (primeira resolução - simples):

print("Digite qual a distância da viagem(km): ")
dist = int(input())

if dist <= 200:
    passagem = dist * 0.50
else:
    passagem = dist * 0.45

print(passagem)

# Exercício da passagem (segunda resolução - mais complexo):
# Considerando que até 200 km é .5 e depois .45:

if dist <= 200:
    passagem = dist * 0.50
else:
    passagem = 200 * 0.50 + (dist - 200) * 0.45

print(passagem)

# Exercício do número entre 1000 e 9999:

while True:
    print("Escreva um número entre 1000 e 9999: ")
    num = int(input())
    if num < 1000 or num > 9999:
        continue
    else:
        strNum = list(str(num))
        strNum.reverse() # O exercício pede pra mostrar da forma inversa (unidade, dezena, centena e milhar)
        for i in strNum:
            print(i)
        break

# Exercício do número com valor flutuante:

print("Digite um valor flutuante: ")
valorFloat = float(input())
print(math.sqrt(valorFloat)) # Raíz quadrada do valor
print(math.ceil(valorFloat)) # Função teto do valor
print(math.floor(valorFloat)) # Função chão do valor
print(math.trunc(valorFloat)) # Parte inteiro do valor

