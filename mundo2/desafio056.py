# Desafio 056:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos
idades = 0
maisvelho = 0
nomevelho = ""
mulheres = 0
for i in range (1, 5):
    nome = str(input(f'Qual o nome da {i}ª pessoa?: ')).strip()
    idade = int(input(f'Qual a idade?: '))
    sexo = str(input(f'Qual o sexo dela, [F/M]?: ')).strip().upper()
    idades += idade
    if idade > maisvelho and sexo == 'M':
        nomevelho = nome
        maisvelho = idade
    if idade < 20 and sexo == 'F':
        mulheres += 1
media = idades / 4
print(f'A média das idades delas é {media}')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomevelho}')
print(f'Ao todo tem {mulheres} mulher(es) com menos de 20 anos')