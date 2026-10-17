import random

v = 0
while True:
    c = random.randint(1, 10)
    n = int(input('Diga um valor: '))
    m = input('Par ou ímpar? [P/I]: ').upper()
    soma = n + c

    print(f'Você jogou {n} e o computador {c}. Total de {soma}', end=' ')
    
    if m == 'P':
        if soma % 2 == 0:
            print('Você venceu!\n')
            v += 1
        else:
            print('Você perdeu!\n')
            break
    elif m == 'I':
        if soma % 2 == 1:
            print('Você venceu!\n')
            v += 1
        else:
            print('Você perdeu!\n')
            break
    else:
        print('Opção inválida!')
        break

print(f'GAME OVER! Você venceu {v} vezes.')
