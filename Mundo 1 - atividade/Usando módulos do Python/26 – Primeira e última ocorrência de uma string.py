# Lê o nome e já transforma em maiúsculas
nome = input('Digite seu nome: ').upper().strip()

# Conta quantas vezes aparece a letra "A"
print(f'A letra A aparece: {(nome.count('A'))} vezes na frase')

# Mostra a posição da primeira ocorrência de "A"
# find() retorna índice começando em 0, por isso somamos +1
print(f'A primeira letra A apareceu na posição: {(nome.find('A') + 1)}')

# Mostra a posição da última ocorrência de "A"
print(f'A última letra A apareceu na posição: {(nome.rfind('A') + 1)}')
