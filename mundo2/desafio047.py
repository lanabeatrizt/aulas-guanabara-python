# Desafio 047: 
# Crie um programa que mostre na tela todos os números pares que estão no interalo entre 1 e 50.
for n in range (1, 51):
    if n % 2 == 0:
        print(n, end=' ')