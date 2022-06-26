#Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e
#peça para o usuário tentar descobiri qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário vendeu ou perdeu

from random import randint
from time import sleep
PC = randint(0, 5) # Faz o pc pensar
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-' *20)
Player = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('LOADING...')
sleep(2)
if Player == PC:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI!! Eu pensei no número {} e não no {}!'.format(PC, Player))




