#ler 3 valores e ver se formam um triangulo

print('-=-'*20)
print('Analisador de Triângulo')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')