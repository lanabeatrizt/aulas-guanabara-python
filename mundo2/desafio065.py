# Desafio 065:
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resposta = 'S'
contador = 0
soma = 0
maior = 0
menor = 0
while resposta in 'Ss':
    numero = int(input('Informe um número: '))
    contador += 1
    soma += numero
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f'Você digitou {contador} números, a média deles foi {soma/contador:.2f}, o maior número foi {maior} e o menor {menor}')