# Desafio 071:
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao 
# usuário qual será o valor a ser sacado (número inteiro) o programa vai informar quantas 
# cédulas de cada valor serão entregues.
# Obs.: considere que o caixa possui cédulas de 50, 20, 10 e 1.
saque = int(input('Qual valor a ser sacado? R$ '))
total = saque
cedulaatual = 200
totalcedulas = 0
print(f'O total de cédulas a serem sacadas será: ')
while True:
    if total >= cedulaatual:
        total -= cedulaatual
        totalcedulas +=1
    else:
        if totalcedulas > 0:
            print(f'{totalcedulas} cédulas de R$ {cedulaatual}')
        if cedulaatual == 200:
            cedulaatual = 100
        elif cedulaatual == 100:
            cedulaatual = 50
        elif cedulaatual == 50:
            cedulaatual = 20
        elif cedulaatual == 20:
            cedulaatual = 10
        elif cedulaatual == 10:
            cedulaatual = 5
        elif cedulaatual == 5:
            cedulaatual = 1
        totalcedulas = 0
        if total == 0:
            break