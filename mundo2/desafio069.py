# Desafio 069:
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados.
# c) quantas mulheres tem menos de 20 anos.
contador18 = contadormasc =  contadorfem20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'mMfF':
        sexo = input('Qual o seu sexo? [F/M] ').strip()[0]
    if idade >= 18:
        contador18 +=1
    if sexo in 'mM':
        contadormasc += 1
    if sexo in 'fF' and idade < 20:
        contadorfem20 += 1
    continuar = ' '
    while continuar not in 'sSnN':
        continuar = input('Quer continuar cadastrando pessoas? [S/N] ').strip()[0] ## por aqui, senão ao dar break, não vai rodar os contadores da última resposta
    if continuar in 'nN':
        break
print(f'''a) {contador18} pessoas cadastradas tem mais de 18 anos.
b) foram cadastrados {contadormasc} homens.
c) {contadorfem20} mulheres cadastradas tem menos de 20 anos.''')