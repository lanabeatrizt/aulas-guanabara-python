# Desafio 057:
# Faça um programa que leia o sexo de uma pessoa, mas, só aceite os valores 'M' ou  'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Digite o seu sexo [M/F]: ').strip().upper()[0]
# [0] para pegar a primeira letra - fatiamento/slice, pq vai que a pessoa digita feminino
# Enquanto o sexo não estiver dentro de 'M', 'm' ou 'F', 'f'
while sexo not in 'MnFf':
    sexo = input('Dados inválidos. Por favor, digite seu sexo [M/F]: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')