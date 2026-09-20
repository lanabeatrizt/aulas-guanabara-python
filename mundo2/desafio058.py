# Desafio 058:
# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.
from random import randint
computador = randint(0, 10)
palpite = 1
jogador = int(input('Tente adivinhar o número que eu pensei, de 0 a 10: '))
while jogador != computador:
    jogador = int(input('Errou, tente novamente: '))
    palpite += 1
print(f'Você acertou, eu escolhi {computador} e você tentou {palpite} vezes até acertar!')