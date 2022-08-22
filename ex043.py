peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do PESO normal.')
elif 18.5 <= imc <25:
    print('PARABÉNS, você está na faixa de PESO normal.')
elif 25 <= imc < 30:
    print('Você esta em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')