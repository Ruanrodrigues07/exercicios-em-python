salario = float(input('Qual o salário do funcionário? R$'))
if salario >= 1250.00:
    novo = (salario * 10 / 100) + salario
else:
    novo = (salario * 15 / 100) + salario
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))
