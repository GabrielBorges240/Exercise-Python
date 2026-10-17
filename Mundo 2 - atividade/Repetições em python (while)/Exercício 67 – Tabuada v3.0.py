numero = int(input('Digite um número para ver a tabuada: '))
soma = 1
while soma <= 10:
    if numero < 0:
        break
    print(f'{numero} x {soma} = {numero * soma}')
    soma += 1