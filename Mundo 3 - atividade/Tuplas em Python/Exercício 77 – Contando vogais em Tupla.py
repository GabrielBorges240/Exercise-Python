palavras = ('Pastel', 'Correr', 'Chiclete', 'Vaca', 'Cavalo',)

for palavra in palavras:
    vogais = sum(letra in 'aeiou' for letra in palavra.lower())
    print(f'Na palavra {palavra.upper()} temos:', end= ' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()