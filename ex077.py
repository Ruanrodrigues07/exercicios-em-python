palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
           'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
           'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavra:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
