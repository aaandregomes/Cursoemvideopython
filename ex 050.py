soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0 and num != 0:
        soma += num
        cont += 1
print('você informou {} números pares e a soma foi {}'.format(cont, soma))

