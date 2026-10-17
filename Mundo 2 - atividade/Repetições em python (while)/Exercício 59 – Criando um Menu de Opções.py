n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))


opção = 0

while opção != 5:  
    print(f'\033[1;32m[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\033[m')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print(f'\033[1;32mA soma de {n1} + {n2} é {soma}.\033[m')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'\033[1;32mA multiplicação de {n1} x {n2} é {multiplicação}.\033[m')
    elif opção == 3:
        if n1 > n2:
            print(f'\033[1;32mO maior número entre {n1} e {n2} é {n1}.\033[m')
        elif n2 > n1:
            print(f'\033[1;32mO maior número entre {n1} e {n2} é {n2}.\033[m')
        else:
            print(f'\033[1;32mOs números são iguais: {n1} = {n2}.\033[m')
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Saindo do programa...')
    else:
        print('\033[1;31mOpção inválida. Tente novamente.\033[1;31m')
    
     