# Desafio 062:
# Melhore o desafio 061, pergutando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10 # Começa valendo 10 pq o programa já deu 10 antes
while mais != 0:
    total = total + mais # O total engole os 10 primeiros, depois engole os extras
    while cont <= total:
        print(f'{termo} ➔ ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados no total.')