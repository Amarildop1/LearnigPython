import random

"""
    Leia um vetor V (contendo 30 elementos inteiros) 
    e um valor inteiro K,
    calcule e exiba a quantidade de ocorrências de K dentro de V.
"""

vetorV = []
cont = 0

#Preenche o vetor com números aleatórios
for i in range(30):
    vetorV.append( int( (random.random())*10 ) )

"""
#Preenche o vetor com uma entrada
for i in range(10):
    vetorV.append(int(input("Digite um número: ")))
"""

k = int(input("\nInforme o valor de 'K': "))

#Contando a quantidade de ocorrências de K em vetorV
for i in range(len(vetorV)):
    if (vetorV[i] == k):
        cont += 1

print("\nVetor A:", vetorV)

if (cont == 0):
    print(f"\nNão há ocorrências do número '{k}' neste vetor!\n")
else:
    print(f"\nOcorrências do número '{k}' no vetor:",cont,)
