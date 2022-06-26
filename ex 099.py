from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    sleep(1.5)
    print(f'O maior valor informado foi {maior}.')
    sleep(1.5)



maior(2, 4, 10, 6, 1, 7)
maior(4, 9, 0)
maior(1, 1)
maior(1, 2)
maior()
