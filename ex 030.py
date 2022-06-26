#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

número = int(input('Me diga um número qualquer: '))
resultado = número % 2
#print('O resultado foi {}'.format(resultado))
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
