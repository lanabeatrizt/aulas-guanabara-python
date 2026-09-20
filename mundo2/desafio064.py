# Desafio 064:
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar 
# quando o usuário digitar o valor 999, que é a condição de parada.
# Mo final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando 
# o flag - o 999).
soma = 0
contador = 0
numero = int(input('Digite um número inteiro [999 para parar]: '))
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número inteiro [999 para parar]: ')) # inverti, pq ai qdo digitar o 999 não vai rodar td do while (funciona tipo um break que vai dar só na próxima aula pelo que chuto)
print(f'Você digitou {contador} números e a soma deles deu {soma}')