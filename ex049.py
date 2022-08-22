num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(0, 11):
    print('{} X {:2} = {:2}'.format(num, c, num*c))
print('Fim')
