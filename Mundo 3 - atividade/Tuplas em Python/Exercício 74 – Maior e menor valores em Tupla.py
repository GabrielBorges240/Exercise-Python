from random import randint
 
numeros = tuple(randint(1, 10) for _ in range(5))

print('Os números sorteados foram:', *numeros)
print(f'O menor valor sorteado foi {min(numeros)}')
print(f'O maior valor sorteado foi {max(numeros)}')

 