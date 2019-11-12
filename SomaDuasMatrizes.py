"""
    Preenche duas matrizes 2x3 com valores inteiros fornecidos pelo usuário. 
    Soma as duas matrizes.
    Armazena o resultado em uma terceira matriz e exibe.
"""

linha = 2
coluna = 3

matrizA = []
matrizB = []
matrizSoma = []

#Preenche com zero
for i in range(linha):
    matrizA.append([0]*coluna)
    matrizB.append([0]*coluna)
    matrizSoma.append([0]*coluna)

#Preenche Matriz A com a entrada
for i in range(linha):
    for j in range(coluna):
        matrizA[i][j] = int(input(f'MatrizA ({i},{j}): '))

#Exibe matriz A
print("\nMatriz A")
for i in range(linha):
    print(matrizA[i])

print("\n---------------------------")

#Preenche Matriz B com a entrada
for i in range(linha):
    for j in range(coluna):
        matrizB[i][j] = int(input(f'MatrizB ({i},{j}): '))

#Exibe matriz B
print("\nMatriz B")
for i in range(linha):
    print(matrizB[i])

print("\n---------------------------")

#Soma as Matrizes
for i in range(linha):
    for j in range(coluna):
        matrizSoma[i][j] = matrizA[i][j] + matrizB[i][j]

#Exibe a soma
print("\nMatriz Soma: ")
for i in range(linha):
    print(matrizSoma[i])

