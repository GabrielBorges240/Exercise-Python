matriz = [[0, 0, 0 ],
          [0, 0, 0], 
          [0, 0, 0]]

pares = 0
terceira_coluna = 0

for linha in range(3):
    for coluna in range(3):
        numero = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
        matriz[linha][coluna] = numero

        if numero % 2 == 0:
            pares += numero

        if coluna == 2:
            terceira_coluna += numero
        
print()
for valor in range(3):
    for valores in range(3):
        print(end= f'[{matriz[valor][valores]}] ')
    print()
print()
print(f'Soma dos valores pares: {pares}')
print(f'Soma da terceira coluna: {terceira_coluna}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')





