num = cont = soma = 0
while num != 999:
    num = int(input('Digite um números [999 para parar]: '))
    if num != 999:
        cont = cont + 1
        soma = soma + num
print('Você digitou {} números e a soma entre eles foi de {}.'.format(cont, soma))
