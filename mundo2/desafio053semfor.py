# Desafio 053:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços.
frase = input('Digite uma frase: ').lower()
nova_frase = frase.replace(" ", "")
if nova_frase == nova_frase[::-1]:
    print(f'É um palíndromo')
else:
    print(f'Não é um palíndromo')