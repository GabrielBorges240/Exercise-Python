valores = []

for cont in range(4):
    valores.append(int(input(f'Digite um valor para a posição {cont}:')))
    print(f'Na posição {cont} encontrei o valor: {valores[cont]}')

maior = max(valores)
menor = min(valores)

pos_maiores = [i for i, v in enumerate(valores) if v == maior]
pos_menores = [i for i, v in enumerate(valores) if v == menor]

print(f'Maior valor {maior} nas posições: {valores.index(maior)}')  # Maior valor: 87
print(f'Menor valor {menor} nas posições: {valores.index(menor)}')
