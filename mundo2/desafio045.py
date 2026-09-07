# Desafio 045:
# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'Vamos jogar Jokenpô!\nSuas opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Qual a sua jogada? '))
print(f'JO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PÔ!!!')
print(f'Eu escolhi: {itens[computador]}')
print(f'Você escolheu: {itens[jogador]}')
if computador == jogador:
    print(f'Empatamos!')
# vitória computador
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print(f'Eu ganhei!')
else:
    print(f'Você ganhou!')
# Guanabara fez diferende, em vaso de opção inválida! Vide arquivo desafio045b.py
# Fiz diferente porque na aula o professor não queria que fizéssemos todas as opções.