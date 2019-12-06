#List08 - Quest02
#Funções
# 05.Dez.2019
#Recebe 3 números e diz qual o menor

def menorEntreOsTres(num1, num2, num3):
    if (num1 < num2 and num1 < num3):
        menor = num1
    elif(num2 < num3):
        menor = num2
    else:
        menor = num3
    return menor


#Programa teste
num = []

for i in range(3):
    num.append(float(input("Digite um número: ")))

menor = menorEntreOsTres(num[0], num[1], num[2])

print("O menor entre os três é:", menor)