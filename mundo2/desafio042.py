# Desafio 042:
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
print(f'Analisador de triângulos. Informe a medida do:')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os seguimentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print(f'Equilátero')
    elif r1 != r2 != r3 != r1:
        print(f'Escaleno')
    else:
        print(f'Isóceles')
else:
    print(f'Os seguimentos acima não podem formar um triângulo.')