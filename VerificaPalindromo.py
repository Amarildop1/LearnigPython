#Verifica se a string é um Palíndromo.
#Author Amarildo - 05.Nov.19
"""
    Palíndromo: Quando uma palavra ou frase pode ser lida 
    iniciando pela esquerda ou pela direita.
"""

cond = True
print("\n----------- Verifica se a string é um Palídromo -----------\n")
while cond != 'fim':
    cond = input("Digite fim para encerrar ou tecle Enter: ")
    if(cond == 'fim'):
        break
    entrada = input("\nDigite a frase: ")
    invert = entrada[ : : -1]
    print("Invertido: ", invert)

    if (invert == entrada):
        print(f'"{invert}", É um palíndromo! \n')
    