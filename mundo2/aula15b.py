numero = soma = 0
while True: # loop infinito
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale: {soma}')