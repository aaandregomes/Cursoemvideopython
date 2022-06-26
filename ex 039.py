#Alistamento militar.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
sexo = str(input('Qual o seu gênero?'))
print('Quem é do sexo {} e nasceu em {} tem {} ano em {}.'.format(sexo, nasc, idade, atual))
if idade == 18 and sexo == 'Masculino':
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18 and sexo == 'Masculino':
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18 and sexo == 'Masculino':
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi {}'.format(ano))
else:
    print('Você não tem a obrigação de se alistar!')




