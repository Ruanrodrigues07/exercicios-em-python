resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp != 'S' and 'N':
        resp = str(input('Tente novamente. Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} e a média foi {}.'.format(quant, media))
print('O maior foi {} e o menor foi {}.'.format(maior, menor))
