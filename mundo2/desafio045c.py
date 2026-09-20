# Desafio 045:
# Crie um programa que faça o computador jogar Jokenpô com você.
# versão depois de aprender o while
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Vamos jogar Jokenpô!')
while True:
    print('Suas opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura')
    jogador = int(input('Qual a sua jogada? '))
    if jogador in (0, 1, 2):
        break
    print('\n❌ Opção inválida! Tente novamente.\n')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print(f'Eu escolhi: {itens[computador]}')
print(f'Você escolheu: {itens[jogador]}')
if computador == jogador:
    print('Empatamos!')
elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    print('Eu ganhei!')
else:
    print('Você ganhou!')