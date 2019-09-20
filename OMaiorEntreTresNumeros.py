#Mostra o maior número entre os três informados.

num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))

if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num1 and num2 > num3):
    print(num2)
else:
    print(num3)