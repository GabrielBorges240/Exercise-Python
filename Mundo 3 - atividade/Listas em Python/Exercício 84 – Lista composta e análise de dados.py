lista = []
dado = ()
menor_peso = float('inf')
maior_peso = float('-inf')

while True:
    nome = input('Nome: ')
    if not nome.isalpha():
                print("Nome inválido. Digite apenas letras.")
                continue
    peso = float(input('Peso: '))
    dado = (nome, peso)
    lista.append(dado)
    maior_peso = max(maior_peso, peso)
    menor_peso = min(menor_peso, peso)
 
    pergunta = input('Quer continuar? [S/N] ').strip().upper()
    if pergunta == 'N':
        break
print(f'Quantidade de pessoas cadastradas: {len(lista)}') 

print(f'Maior peso: {maior_peso}kg. Peso de: ', end='')
for pessoa in lista:
  if pessoa[1] == maior_peso:
    print(f'[{pessoa[0].capitalize()}] ', end='')
print()

print(f'Menor peso: {menor_peso}kg. Peso de: ', end='')
for pessoa in lista:
  if pessoa[1] == menor_peso:
    print(f'[{pessoa[0].capitalize()}] ', end='')
print()

     


 