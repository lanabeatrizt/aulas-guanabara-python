# Desafio 060:
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex. 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Digite um número para calcular o seu fatorial: '))
contador = numero
fatorial = 1

print(f'{numero}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    
    if contador > 1:
        print(' x ', end='') # Se não for o último número, bota o 'x'
    else:
        print(' = ', end='') # Se for o 1 (último número), bota o '='
    
    fatorial *= contador # fatorial = fatorial * contador
    contador -= 1

print(fatorial)