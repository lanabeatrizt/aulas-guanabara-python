# Desafio 067:
# Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado 
# for negativo.
numero = contador = 0
while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    for contador in range (1, 11):
        tabuada = numero * contador
        print(f'{numero} x {contador} = {tabuada}')
print('Programa de tabuada encerrado')