# Desafio 054:
# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a 
# maioridade e quantas já são maiores.
from datetime import date
MAIORIDADE = 18
hoje = date.today().year
menor = 0
maior = 0
for c in range (1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = hoje - nascimento
    c += 1
    print (f'Então ela tem {idade} anos')
    if idade < MAIORIDADE:
        print(f'E portanto é menor de idade')
        menor += 1
    else:
        print(f'E portanto é maior de idade')
        maior +=1
print(f'No total {menor} pessoas são menores e {maior} pessoas são maiores')