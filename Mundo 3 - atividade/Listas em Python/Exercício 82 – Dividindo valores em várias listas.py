lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número:'))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]:').strip().upper() 
    if continuar == 'N':
        break
    
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')
print(f'Todos os números digitados foram: {lista}')
    
