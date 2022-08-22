preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção com desconde de 5% vai custar R${:.2f}'.format(preco, novo))
