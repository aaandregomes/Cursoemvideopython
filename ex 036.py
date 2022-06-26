#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então será negado

casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar?'))
prestações = casa / (anos * 12)
mínimo = salário * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos),end='')
print('a prestação será de R$ {:.2f}'.format(prestações))
if prestações <= mínimo:
    print('Compra aceita!')
else:
    print('Compra negada!')






