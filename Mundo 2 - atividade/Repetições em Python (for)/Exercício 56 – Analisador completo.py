homem_mais_velho = None
idade_homem = 0
soma_idade = 0
total_mulheres_menor_20 = 0

for c in range(1, 5):
    nome = input(f"qual o nome da {c}° pessoa? ")
    sexo = input(f"qual o sexo de {nome}? (M/F) ")
    idade = int(input(f"qual a idade de {nome}? "))
    
    soma_idade += idade
    
    if sexo.upper() == "M":
        if idade > idade_homem:
            homem_mais_velho = nome
            idade_homem = idade
    
    if sexo.upper() == "F" and idade < 20:
        total_mulheres_menor_20 += 1

media_idade = soma_idade / 4
print(f'a média de idade do grupo é de {media_idade:.1f} anos') 
print(f"o nome do homem mais velho é {homem_mais_velho}")
print(f"ao todo são {total_mulheres_menor_20} mulheres com menos de 20 anos")