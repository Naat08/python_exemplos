aluno = input('Digite o nome do aluno:')
notal = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
falta = int(input('Digite a quantidade de faltas: '))
media = (notal+nota2+nota3)/3
print('Aluno: ' + aluno)
print('Média: ' + str(media))
print('Falta(s): ' + str(falta))