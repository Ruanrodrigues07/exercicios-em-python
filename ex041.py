from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL.')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR.')
elif 19 < idade <= 20:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER')
