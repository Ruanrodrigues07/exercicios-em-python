from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu Palpite? '))
    palpite = palpite + 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas'.format(palpite))
