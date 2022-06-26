num = [2, 5, 9, 1]
num[2] = 3
'''Trocou o numero na posição 2 pelo 3. lembrando que começa no 0.'''
num.append(7)
'''add esse valor a lista'''
num.sort(reverse=True)
'''Organiza a lista em ordem inversa'''
num.insert(2, 2)
'''agrega o numero 2, na posição 2.'''
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos!')


