# Aula 15: break
contador = 1
while True: # se não por um break, vai entrar em loop infinito
    print(contador, end=' ')
    contador += 1
    if contador == 5:
        break
print(f'Acabou')