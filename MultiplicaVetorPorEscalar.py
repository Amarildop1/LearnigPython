vetorA = []
vetorB = []

N = int(input("\nInforme a quantidade de elementos do vetor: "))

for i in range(N):
    vetorA.append(int(input(f"Digite o {i+1}º elemento: ")))

K = int(input("\nDigite um número inteiro: "))

for i in range(len(vetorA)):
    vetorB.append(vetorA[i] * K)

print("\nVetor A:", vetorA)

print(f"\nMultiplicando pelo escalar '{K}' é gerado o vetor B:", vetorB)
print()

"""
    Leia um vetor A de N números inteiros (N será lido), 
    e um número inteiro K.
    Construa e exiba um outro vetor B,
    cujos elementos são os elementos de A[] * K.
"""
#L4-Q2 - 12.Nov.2019