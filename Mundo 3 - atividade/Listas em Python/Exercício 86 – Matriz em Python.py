matriz = [[0, 0, 0 ],[0, 0, 0], [0, 0, 0]]

for valor in range(3):
    for valores in range(3):
        numero = int(input(f'Digite um valor para [{valor}][{valores}]: '))  
        matriz[valor][valores] = numero

for valor in range(3):
    for valores in range(3):
        print(end= f'[{matriz[valor][valores]}] ')
    print()