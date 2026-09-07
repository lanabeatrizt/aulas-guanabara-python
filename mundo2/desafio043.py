# Desafio 043:
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a 
# tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em m: '))
imc = peso / (altura ** 2)
ABAIXO = 18.5
IDEAL = 25
SOBREPESO = 30
OBESIDADE = 40
print(f'Seu IMC é {imc:.1f} e você está: ')
if imc < ABAIXO:
    print(f'Abaixo do Peso')
elif imc < IDEAL:
    print(f'No peso ideal')
elif imc < SOBREPESO:
    print(f'Em Sobrepeso')
elif imc < OBESIDADE:
    print(f'Em Obesidade')
else:
    print('Em Obesidade mórbida')