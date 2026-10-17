soma = 0
countador = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    print(f'Você digitou {n}.')
    soma += n
    countador += 1
print(f'a soma é: {soma}')
print(f'o contador é: {countador}')