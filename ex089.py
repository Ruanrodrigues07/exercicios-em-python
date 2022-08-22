from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
sleep(0.5)
print('-=' * 30)
sleep(0.5)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
sleep(0.5)
print('-' * 26)
sleep(0.5)
for i, a in enumerate(ficha):
    sleep(0.5)
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    sleep(0.5)
while True:
    sleep(1)
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
    if opc > len(ficha) - 1:
        opc = int(input('Aluno inválido! Tente novamente! (999 interrompe): '))
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print(f'{" VOLTE":<>20} {"SEMPRE ":><20}')
