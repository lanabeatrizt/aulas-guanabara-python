# Desafio 052:
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número inteiro: '))
total_divisores = 0
for i in range (1, numero + 1):
   if numero % i == 00:
      total_divisores += 1
print(f'O número {numero} foi divisível {total_divisores} vezes.')
if total_divisores == 2:
   print(f'E por isto ele é primo')
else:
   print(f'E por isto ele não é primo')