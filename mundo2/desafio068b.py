# versão do Guanabara, pois fiz diferente
from random import randint

v = 0
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    
    # Validação para prender o usuário até ele digitar 'P' ou 'I'
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    
    # Checagem de vitória ou derrota
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0: # Ou total % 2 == 1
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
            
    print('Vamos jogar novamente...')
    print('-=' * 15)

print(f'GAME OVER! Você venceu {v} vezes.')