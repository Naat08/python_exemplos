nota1 = int(input('Informe a nota do 1º Bimestre (0-100): '))
nota2 = int(input('Informe a nota do 2º Bimestre (0-100)'))
media = (nota1+nota2)
if media >= 60:
    print(f'Você foi aprovado com a média {media}')
else:
    print(f'Você não foi aproveira, sua média {media}')
