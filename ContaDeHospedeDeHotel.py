#@Author Amarildo
#L2-Q10 - 25.set.2019
#Pequeno Sistema de um hotel. (Não salva dados)
'''
Recebe Nome, tipo de apartamento, quantidade de diárias e 
valor de consumo interno.
Retorna a conta final detalhada de um hóspede, 
com base em alguns critérios.
[Assume um usuário perfeito!]
'''
print("\n------------- Hotel PythonHouse -------------")
nomeDoHospede = input("\nInforme o nome do hóspede: ")
tipoDeApto = input("Informe o tipo de apartamento(A,B,C ou D): ")
numeroDeDiarias = int(input("Quantas diárias? "))
valorDoConsumo = float(input("Qual o valor do consumo interno? R$ "))

if(tipoDeApto == 'A'):
    valorTotalDasDiarias = numeroDeDiarias * 150.00
elif(tipoDeApto == 'B'):
    valorTotalDasDiarias = numeroDeDiarias * 100.00
elif(tipoDeApto == 'C'):
    valorTotalDasDiarias = numeroDeDiarias * 75.00
elif(tipoDeApto == 'D'):
    valorTotalDasDiarias = numeroDeDiarias * 50.00

subtotal = (valorTotalDasDiarias + valorDoConsumo)
taxaDeServiço = (0.10 * subtotal)

valorTotalGeral = (subtotal + taxaDeServiço)

print("\n------------- Conta do Hóspede --------------")
print("Nome:\t\t\t", nomeDoHospede, 
        "\nTipo de Apto.: \t\t", tipoDeApto,
        "\nQuantidade de diárias: \t", numeroDeDiarias,
        "\nValor da diária: \tR$", (valorTotalDasDiarias/numeroDeDiarias),
        "\nConsumo interno: \tR$", valorDoConsumo,
        "\nSubtotal: \t\tR$", subtotal,
        "\nTaxa de serviço: \tR$", taxaDeServiço,
        "\nTotal Final:\t\tR$", valorTotalGeral)

print("\n------- Copyright © Hotel PythonHouse -------\n")
