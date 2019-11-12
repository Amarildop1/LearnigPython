"""
    Dada uma matriz quadrada de elementos inteiros e ordem N,
    exiba os elementos da diagonal principal.
    Isto é, os elementos onde I = J. Obs: N será lido (N <= 10).
"""

matriz = []
N = int(input("\nDigite a ordem 'N' da matriz: "))

#Preenchendo com zeros
for i in range(N):
    matriz.append(N*[0])

#Preenchendo com a entrada
for i in range(N):
    for j in range(N):
        matriz[i][j] = int(input(f'Matriz ({i},{j}): '))

#Exibindo a matriz completa
print("\nMatriz Quadrada: ")
for i in range(N):
    print(matriz[i])

#Exibindo elementos da diagonal
print("\nElementos da Diagonal: ")
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if(matriz[i] == matriz[j]):
            print(matriz[i][j])
