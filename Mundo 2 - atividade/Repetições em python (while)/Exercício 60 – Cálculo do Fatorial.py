n = int(input('Digite um fatorial: '))

fatorial = 1
contador = n

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f'\033[1;32mO fatorial de {n} é {fatorial}.\033[m')   