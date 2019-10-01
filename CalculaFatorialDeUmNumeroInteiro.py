#Calcula o fatorial de um número inteiro

numero = int(input("Informe um número: "))
cont = 0
fatorial = 1
while (cont < numero):
    cont = cont + 1
    fatorial = fatorial * cont
print(f"O fatorial de {numero} é: ", fatorial)
