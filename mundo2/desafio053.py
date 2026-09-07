# Desafio 053:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços.
frase = input('Digite uma frase: ').lower().strip()
nova_frase = frase.replace(" ", "")
frase_invertida = ""
for letra in range(len(nova_frase) - 1, -1, -1):
    frase_invertida += nova_frase[letra]
if nova_frase == frase_invertida:
    print(f'É um palíndromo')
else:
    print(f'Não é um palíndromo')