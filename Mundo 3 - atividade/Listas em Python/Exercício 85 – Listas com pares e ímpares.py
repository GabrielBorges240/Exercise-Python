lista = []
pares = []
ímpares = []

for numeros in range(1, 8):
    numero = (input(f'Digite o {numeros}º numero: '))
    if not numero.isdigit():
        print('Digito inválido. Digite apenas números.')
        continue
    lista.append(int(numero))     
    
lista.sort()

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        ímpares.append(numero)

print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {ímpares}')