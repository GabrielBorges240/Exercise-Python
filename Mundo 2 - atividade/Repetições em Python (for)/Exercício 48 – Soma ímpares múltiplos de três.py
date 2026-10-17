soma = 0  # Inicializa a variável soma com zero
for número in range(1, 501):  # Loop de 1 a 50
    if número % 3 == 0:  # Verifica se o número é múltiplo de 3
        print(f'{número} é múltiplo de 3')
        soma += número
    else:  # Caso contrário, o número não é múltiplo de 3
        print(f'{número} não é múltiplo de 3')
      # Adiciona o número à soma se for múltiplo de 3
print(f'A soma dos números múltiplos de 3 é: {soma}')  # Exibe a soma dos números múltiplos de 3
