# Desafio 041:
# A Confedereção Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
from datetime import date
MIRIM = 9
INFANTIL = 14
JUNIOR = 19
SENIOR = 25
data_nascimento = int(input('Informe o ano de nascimento do atleta, com 4 dígitos: '))
ano_atual = date.today().year
idade = ano_atual - data_nascimento
print(f'O atleta tem {idade} anos e a categoria é:')
if idade <= MIRIM:
    print(f'MIRIM')
elif idade <= INFANTIL:
    print(f'INFANTIL')
elif idade <= JUNIOR:
    print(f'JÚNIOR')
elif idade <= SENIOR:
    print(f'SÊNIOR')
else:
    print(f'MASTER')