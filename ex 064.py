num = cont = soma = 0
num = int(input('Digíte um número ou [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número ou [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))