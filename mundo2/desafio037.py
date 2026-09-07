# Desafio 037:
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
numero = int(input('Informe um número inteiro qualquer: '))
base = int(input('Escolha a base de conversão:\n[1] para binário\n[2] para octal\n[3] para hexadecimal: '))
if base == 1:
    print(f'O {numero} em binário é: {bin(numero)[2:]}')
elif base == 2:
    print(f'O número {numero} em octal é: {oct(numero)[2:]}')
elif base == 3:
    print(f'O número {numero} em hexadecimal é: {hex(numero)[2:]}')
else:
    print(f'Você não selecionou uma base válida. Tente novamente.')