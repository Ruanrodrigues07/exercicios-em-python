times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians',
         'Bragantino', 'Fortaleza', 'Fluminense', 'América-MG',
         'Ceará=MG', 'Internacional', 'Santos', 'São Paulo',
         'Atlético-GO', 'Juventude', 'Cuiabá', 'Athletico-PR',
         'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')
# print(f'Lista de times do Brasileirão:')
# for t in times:
#     print(f'{t}')
# print('-=' * 15)
# print('Os 5 primeiros são: ')
# for t in times[:5]:
#     print(t)
# print('-=' * 15)
# print('Os 4 últimos times são: ')
# for t in times[-4:]:
#     print(f'{t}')
# print('-=' * 15)
# print('Times em ordem alfabética: ')
# for t in sorted(times):
#     print(f'{t}')
# print('-=' * 15)
# print('O Chapecoense está na: ')
# print(f'{times.index("Chapecoense")+1}ª posição.')
# print('-=' * 15)

print('-' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')

