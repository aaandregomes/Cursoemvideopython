"""Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções,argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.
def contador(i, f, p):

    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p:passo da contagem
    :return: Sem retono
    Função criada por André Gomes

    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


help(contador)

def somar(a=0, b=0, c=0):
    s= a + b + c
    print(f'A soma vale: {s}')


somar()"""

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(0)
print(f'Os resultados são {f1}, {f2} e {f3}')


