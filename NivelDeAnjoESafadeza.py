dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mes (Ex.: 1 ate 12): "))
ano = int(input("Informe o ano: "))

safadeza = (mes + (ano/100) * (50-dia) ) / 10
anjo = (100 - safadeza)

print("\n----- Resultado -----")
print(safadeza,"% Safadeza: ")
print(anjo, "% Anjo: ")