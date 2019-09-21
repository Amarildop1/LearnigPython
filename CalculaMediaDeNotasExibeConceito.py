'''
Calcula a media de aproveitamento através das notas de provas e exercícios 
e exibe o Conceito obtido pelo aluno.
'''
matricula = int(input('Informe a matrícula: '))
nota1 = float(input('Informe a 1ª Nota: '))
nota2 = float(input('Informe a 2ª Nota: '))
nota3 = float(input('Informe a 3ª Nota: '))
mediaExercicios = float(input('Informe a média dos exercicios: '))

mediaAproveitamento = (nota1 + (nota2*2) + (nota3*3) + mediaExercicios)/7

if(mediaAproveitamento < 4.0):
    conceito = 'E'
elif(mediaAproveitamento <= 6.0):
    conceito = 'D'
elif(mediaAproveitamento <= 7.5):
    conceito = 'C'
elif(mediaAproveitamento < 9.0):
    conceito = 'B'
else:
    conceito = 'A'

print('Matrícula:', matricula,
    '\nMédia de Aproveitamento:', mediaAproveitamento,
    '\nConceito:', conceito)

if(conceito == 'A' or conceito == 'B' or  conceito == 'C'):
    print('APROVADO.')
else:
    print('REPROVADO.')