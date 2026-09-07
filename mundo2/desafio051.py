# Desafio 051:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritimética). 
# No final mostre os 10 primeiros termos dessa progressão.
termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = termo + (10 - 1) * razao
for c in range (termo, decimo + razao, razao): #decimo + razão pq em python para no antes do numero colocado no termo final do range, senão ele vai me mostrar apenas 9 termos
    print(c, end=" ")