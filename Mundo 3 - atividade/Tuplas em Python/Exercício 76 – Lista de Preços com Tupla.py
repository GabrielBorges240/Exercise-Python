produtos = ('pão', 1, 'leite', 3.50, 'pastel', 5.10, )

for posicao in range(0, len(produtos), 2):
    nome = produtos[posicao]
    preco = produtos[posicao + 1]
    print(f'{nome:.<30} R${preco:>5.2f}')