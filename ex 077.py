Palavras = ('Aprender', 'Programar', 'Linguagem', 'Phyton', 'Curso', 'Gratis', 'Estudar','Aprendiz')
for p in Palavras:
    print(f'\nNa paralavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
