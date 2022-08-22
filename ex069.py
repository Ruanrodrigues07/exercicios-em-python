tot18 = totmasc = totfem = 0
while True:
    print('-' * 30)
    print('{:' '^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totmasc += 1
    if sexo == 'F' and idade < 20:
        totfem += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^30}')
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totmasc} homens cadastrados')
print(f'E temos {totfem} mulheres com menos de 20 anos')
