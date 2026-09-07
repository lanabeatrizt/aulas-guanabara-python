# Desafio 052:
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número inteiro: '))
total_divisiveis = 0
for i in range (1, numero + 1):
   if numero % i == 00:
      print(f'\033[33m')
      total_divisiveis += 1
   else:
     print(f'\033[31m')
   print(i, end = " ")
print(f'O número {numero} foi divisível {total_divisiveis} vezes.')
if total_divisiveis == 2:
   print(f'E por isto ele é primo')
else:
   print(f'E por isto ele não é primo')