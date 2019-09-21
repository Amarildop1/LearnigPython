peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

IMC = peso / (altura**2)

if(IMC < 26):
    print('IMC:',IMC, '\nNormal.')
elif(IMC < 30):
    print('IMC:', IMC, '\nObeso.')
else:
    print('IMC:', IMC, '\nObesidade Mórbida.')
