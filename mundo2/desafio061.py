# Desafio 061:
# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos 
# da progressão usando a estrutura while.
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
t = 0
while t < 10:
    print(termo, end= " ")
    termo = termo + razao
    t += 1
# Guanabara fez diferente