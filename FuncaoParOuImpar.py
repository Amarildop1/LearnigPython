#List08 - Quest04
#Funções
# 05.Dez.2019
#Função diz se o número é par ou ímpar.
"""
    Programa principal recebe vários números e 
    conta quantos são pares e quantos são ímpares.
"""

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


#Programa teste
qtdePar = 0
totalNum = 0

while True:
    entrada = int(input("Digite um número: "))
    if entrada == 0:
        break
    totalNum += 1
    qtdePar += par(entrada)

qtdeImpar = totalNum - qtdePar

print("\nQuantidade de números pares:", qtdePar)
print("Quantidade de números ímpares", qtdeImpar)


