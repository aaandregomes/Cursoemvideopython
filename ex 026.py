#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A". Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparace {} vezes na frase.' .format(frase.count('A')))
print('A primera letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
