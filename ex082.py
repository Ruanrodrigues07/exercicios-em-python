num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(num)
    elif v % 2 == 1:
        impares.append(num)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pare é {pares}')
print(f'A lista de ímpares é {impares}')
