'''
Leia um número N, inteiro, e some todos os números de 1 até N,
mostrando o resultado.
'''
numero = int(input("Informe um número: "))
cont = 0
soma = 0
while (cont < numero):
    cont = cont + 1
    soma = soma + cont
print(f"Soma dos números até {numero}: ", soma)
