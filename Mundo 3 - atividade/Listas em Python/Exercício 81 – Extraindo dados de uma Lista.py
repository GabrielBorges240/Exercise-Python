lista = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]:').strip().upper() 
    if continuar == 'N':
        break

print(f'Você digitou os valores: {lista}')
print(f'Quantidade de itens {len(lista)} da lista')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')

