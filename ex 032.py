#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
#ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).
#!= (diferente)
from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

