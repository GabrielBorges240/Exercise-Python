numero = int(input('Digite um número:'))
if numero % 2 == 0:
    print(f'o número \033[1;32m{numero}\033[m é par!')
else:
    print(f'o número \033[1;33m{numero}\033[m é ímpar!')  