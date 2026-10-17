numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite outro número:'))
numero3 = int(input('Dgite mais um número:'))
numero4 = int(input('Digite o último número:'))

numeros = (numero1, numero2, numero3, numero4)

print(f'Você digitou os valores: {numeros}')
print(f'Quantas vezes apareceu o valor 9: {numeros.count(9)}')
print(f'Posição em que foi digitado o primeiro valor 3: {numeros.index(3) + 1 if 3 in numeros else "não foi digitado"}')
print(f'Os valores pares digitados: {tuple(numero for numero in numeros if numero % 2 == 0)}')