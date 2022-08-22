distancia = float(input('Qual a distância da viagem? '))
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
