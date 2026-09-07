# Desafio 036:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário? R$ '))
anos = int(input('Em quantos anos vai pagar?: '))
prestacao = casa / (anos * 12)
minimo = salario * (30 / 100)
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print(f'Empréstimo aprovado')
else:
    print(f'Empréstimo negado')