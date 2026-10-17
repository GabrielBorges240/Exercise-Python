maior = 0
menor = 0 

for c in range(1, 6):
    peso = float(input(f"qual o peso da {c}° pessoa? "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"o maior peso lido foi {maior} kg.")
print(f"o menor peso lido foi {menor} kg.")
