# Desafio 063: 
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n 
# primeiros elementos de uma sequência Fibonacci.
# ex.: 0, 1, 1, 2, 3, 5, 8
t1 = 0
t2 = 1
numero = int(input('Quantos termos você quer mostrar da sequência Fibonacci? '))
print(f'{t1} → {t2}', end=' ')
contador = 3 # pq já mostrei o primeiro e segundo termo
while contador <= numero:
    t3 = t1 + t2
    print(f'→ {t3}', end=' ')
    t1 = t2
    t2 = t3
    contador +=1
print('→ Fim')