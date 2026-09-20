# Desafio 068:
# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias 
# consecutivas que ele conquistou no final do jogo.
# obs. pede o valor e se é par ou ímpar, ai soma os valores que cada um escolhe e vê se é par ou ímpar
from random import randint
escolhacomputador = ""
contador = 0
while True:
    escolhajogador = input('Escolha par ou ímpar [P/I]: ').strip().upper()[0]
    while escolhajogador not in 'PI':
        escolhajogador = input('Escolha par ou ímpar [P/I]: ').strip().upper()[0]
    jogador = int(input('Digite o número escolhido: '))
    computador = randint(0, 11)
    soma = jogador + computador
    if escolhajogador == 'P':
        escolhacomputador = 'I'
    else:
        escolhacomputador = 'P'
    if escolhajogador == 'P' and soma % 2 == 0 or escolhajogador == 'I' and soma % 2 != 0:
        print(f'Você escolheu {escolhajogador} e o número {jogador}, eu escolhi {escolhacomputador} e o número {computador}, então você ganhou')
        contador +=1
    else:
        print(f'Você escolheu {escolhajogador} e o número {jogador}, eu escolhi {escolhacomputador} e o número {computador}, então você perdeu')
        break
print(f'Total de suas vitórias: {contador} vitórias, parabéns!')