soma = 0  # Inicializa a variável soma com zero
for número in range(1, 7):  # Loop de 2 a 500 (números pares)
         
    número = int(input(f'Digite o {número}º número:'))  # Converte o número para inteiro
    if número % 2 == 0:    # Verifica se o número é par
       soma += número 
print(f'A soma dos números pares é: {soma}')  # Exibe a soma dos números pares
   # Exibe a soma dos números ímpares  
