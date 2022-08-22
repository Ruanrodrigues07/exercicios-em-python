while True:
    print('-' * 30)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c:2} = {num*c:2}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')