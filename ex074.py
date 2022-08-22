from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
# maior = 0
# menor = 0
# for n in numeros:
#     print(f'{n} ', end='')
#     if n == numeros[0]:
#         menor = n
#         maior = n
#     elif n < menor:
#         menor = n
#     elif n > maior:
#         maior = n
# print(f'\nO maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
