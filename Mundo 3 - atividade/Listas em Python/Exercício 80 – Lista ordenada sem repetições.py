valores = []

for cont in range(4):
    n = int(input('Digite um valor:'))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        for pos in range(len(valores)):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break

print(f'\033[1;33m{"-=" * 30}\033[m')
print(f'Os valores digitados em ordem foram {valores}')