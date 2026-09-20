# Desafio 070:
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá 
# perguntar se o usuário vai continuar. No final, mostre:
# a) qual é o total gasto na compra.
# b) quantos produtos custam mais de R$ 1000.
# c) qual é o nome do produto mais barato.
contadorprodmil = total = contadorprodutos = 0
nome = ' '
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$ '))
    contadorprodutos += 1
    total += preco
    if preco > 1000:
        contadorprodmil += 1
    if contadorprodutos == 1 or preco < maisbarato:
        maisbarato = preco
        nomemaisbarato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja registrar mais produtos? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'''a) O Total da compra foi: R$ {total:.2f}
b) {contadorprodmil} produto(s) custa(m) mais de R$ 1.000,00
c) O nome do produto mais barato foi: {nomemaisbarato}, que custou R$ {maisbarato}''')