nome = input('Informe o nome do cliente: ')
saldoMedio = float(input('Informe o saldo médio: '))

if(saldoMedio <= 200):
    print('Nenhum Crédito!')
elif(saldoMedio <= 400):
    print('----- Informações -----')
    credito = saldoMedio + (saldoMedio * 0.20)
    print("Cliente:",nome,"\nSaldo Médio:",saldoMedio, "\nCrédito:", credito,)
elif(saldoMedio <= 600):
    print('----- Informações -----')
    credito = saldoMedio + (saldoMedio * 0.30)
    print("Cliente:",nome,"\nSaldo Médio:",saldoMedio, "\nCrédito:", credito,)
else:
    print('----- Informações -----')
    credito = saldoMedio + (saldoMedio * 0.40)
    print("Cliente:",nome,"\nSaldo Médio:",saldoMedio, "\nCrédito:", credito,)
