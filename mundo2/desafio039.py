# Desafio 039:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo.
from datetime import date
ano_nascimento = int(input('Qual o ano de seu nascimento com 4 dígitos: '))
ALISTAMENTO = 18
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos.')
if idade < ALISTAMENTO:
    print(f'Ainda falta(m) {ALISTAMENTO - idade} ano(s) para o alistamento!')
elif idade == ALISTAMENTO:
    print(f'É hora de se alistar!')
else:
    print(f'Já passou/passaram {idade - ALISTAMENTO} ano(s) do prazo do alistamento!')