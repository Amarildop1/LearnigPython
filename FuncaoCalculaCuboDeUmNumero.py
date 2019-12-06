#List08 - Quest01
#Funções
# 05.Dez.2019
#Recebe um valor do tipo float e calcula o cubo.

def cubo(num):
    return num**3

    
num = float(input("Digite um número: "))

cuboDeNum = cubo(num)

print(cuboDeNum)