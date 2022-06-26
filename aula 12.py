nome = str(input('Qual é seu nome? '))
if nome == 'André':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Marcos' or nome == 'Maria':
    print('Seu nome é muito comum no brasil!')
else:
    print('Que nome diferente!')
print('Tenha  um bom dia, {}'.format(nome))

