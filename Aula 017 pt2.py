'''valores = []
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
#valores.append(5)
#valores.append(9)
#valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''
a = [2, 3, 4, 7]
b = a[:]
'''Com isso ele cria uma copia de B em A. se for " = " ele cria uma ligação. '''
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
