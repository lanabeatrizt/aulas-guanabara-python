# Desafio 044:
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
preco_normal = float(input('Digite o valor do produto: R$ '))
forma = int(input('Digite a forma de pagamento:\n[1] à vista em dinheiro/cheque\n[2] à vista no cartão\n[3] em 2x no cartão\n[4] em 3x ou mais no cartão: '))
vista = 0.1
vista_cartao = 0.05
duas_vezes = preco_normal
tres_vezes = 0.2
if forma == 1:
    preco_novo = preco_normal - (preco_normal * vista)
elif forma == 2:
    preco_novo = preco_normal - (preco_normal * vista_cartao)
elif forma == 3:
    preco_novo = preco_normal
    parcela = preco_novo / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f}.')
elif forma == 4:
    preco_novo = preco_normal + (preco_normal * tres_vezes)
    total_parcelas = int(input('Em quantas parcelas?'))
    parcela = preco_novo / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f}, com juros.')

else:
    preco_novo = preco_normal
    print(f'Opção inválida de pagamento, tente novamente!')
print(f'O valor a ser pago é R$ {preco_novo:.2f}')