# Aula 11: Cores ASCII
# Exemplo: \033[0;33;44m 
# [ style ; text ; back m
# style 0 none, 1 bold, 4 underline e 7 negative
# text cores usando números 30 até 37
# back idem mas é 40 até 47
# Ex.:
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[0;30;42m
# \033[m
# \033[7;30m
nome = input('Qual seu nome? ')
print(f'\033[1;32;43mOlá,\033[4;36;44m{nome}!\033[m')
print(f'\033[4;30;45mVeja meu teste de cores!\033[m')
# dá pra criar variáveis pra por cores e/ou limpar, pra não ter que ficar digitando esses códigos