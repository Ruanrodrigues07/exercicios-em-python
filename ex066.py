soma = cont = 0
while True:
    num = int(input('Digite um valor(999 para parar: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma de {cont} valores foi {soma}!.')
