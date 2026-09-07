# Desafio 049:
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora 
# utilizando um laço for.
numero = int(input('Escolha um número inteiro para fazer a tabuada: '))
for i in range (0, 11):
    tabuada = numero * i
    print(f'{numero} x {i} = {tabuada}')