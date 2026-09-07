# Desafio 053:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços.
frase = input('Digite uma frase: ').lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
   inverso += junto[letra]
if inverso == junto:
   print('É um palíndromo')
else:
   print('Não é um palíndromo')