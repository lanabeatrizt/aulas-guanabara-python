# Desafio 055:
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o 
# menor peso lidos.
peso_maior = 0
peso_menor = 0
for p in range (1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa em kg: '))
    if p == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f'O maior peso é: {peso_maior:.1f}kg e o menor é {peso_menor:.1f}kg')