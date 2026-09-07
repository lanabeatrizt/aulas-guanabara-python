# Desafio 038:
# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
numero1 = int(input('Digite um primeiro número inteiro: '))
numero2 = int(input('Digite um segundo número: '))
if numero1 > numero2:
    print(f'O primeiro número é maior')
elif numero2 > numero1:
    print(f'O segundo número é maior')
else:
    print(f'Não existe valor maior, os dois são iguais')