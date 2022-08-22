from time import sleep
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        produto = num1 * num2
        print('A multiplicação de {} X {} é {}'.format(num1, num2, produto))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('informe os núeros novamente:')
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
    sleep(2.5)
print('Fim do programa! volte sempre!')
