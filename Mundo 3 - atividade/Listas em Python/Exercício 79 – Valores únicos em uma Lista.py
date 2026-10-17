valores = []

while True:
    valor = int(input(f'Digite um valor:'))
    if valor not in valores:
       valores.append(valor)
       print('Valor Adicionado com sucesso!')

    else:
        print('Valor duplicado. Não vou adicionar.')

    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar == "N":
        break

valores.sort()
print(f'Você digitou os valores únicos: {valores}')