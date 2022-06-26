#Faça um programa que leia o nome completo de uma pessoa mostranfo em seguida o primeiro e o ultimo nome separadamente

n = str(input('Digite seu nome completo: '))
nome = n.split()
#split separa o nome por palavras e uma lista
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
