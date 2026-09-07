# Aula 12: Condições Aninhadas
nome = str(input('Qual é se nome?' ))
if nome == 'Lana':
    print(f'Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popular por aqui!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print(f'Que belo nome feminino!')
else:
    print(f'Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')