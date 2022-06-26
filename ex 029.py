#Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80km/h, mostre uma mensagem
#dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

Velocidade = float(input('Velocidade do carro? '))
if Velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (Velocidade-80) * 7
    print('Você deve pegar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

