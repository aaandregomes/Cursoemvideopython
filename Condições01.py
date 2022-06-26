n1 = float(input('Valor da primeira nota: '))
n2 = float(input('Valor da segunda nota: '))
m = (n1 +n2)/2
print('A sua média foi: {:.1f}'.format(m))
if m>= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')



