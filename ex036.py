casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
prestacacao = casa / (ano * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end=' ')
print(' a prestação será de R${:.2f}'.format(prestacacao))
if prestacacao <= minimo:
    print('Empréstimo pode ser CONSEDIDO!'.format(prestacacao))
else:
    print('Empréstimo NEGADO'.format(prestacacao))
