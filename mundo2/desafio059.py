# Desafio 059:
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
numero1 = int(input('Digite o valor 1: '))
numero2 = int(input('Digite o valor 2: '))
menu = 0
while menu is not 5:
    menu = int(input('''Digite:
[1] para somar
[2] para multiplicar
[3] para ver o maior número
[4] para digitar novos números
[5] para sair do programa: '''))
    if menu == 1:
        print(f'A soma é: {numero1 + numero2}')
    elif menu == 2:
        print(f'A multiplicação é {numero1 * numero2}')
    elif menu == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é o maior')
        else:
            print(f'O número {numero2} é o maior')
    elif menu == 4:
        numero1 = int(input('Digite o valor 1: '))
        numero2 = int(input('Digite o valor 2: '))
    else:
        print('Opção inválida, tente novamente')
print('Você saiu do programa!')