#Recebe a idade de um nadador e mostra sua modalidade.

idade = int(input('Informe a idade do nadador: '))

if(idade < 5):
	print('Você ainda não atingiu a idade.')
elif(idade <= 7):
    print('Infantil A')
elif(idade <= 10):
    print('Infantil B')
elif(idade <= 13):
    print('Juvenil A')
elif(idade <= 17):
    print('Juvenil B')
else:
    print('Adulto')
