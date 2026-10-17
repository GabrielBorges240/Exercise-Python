total_homens = 0
total_mulheres_menores_20 = 0
total_pessoas_mais_18 = 0

while True:
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo (M/F): ").strip().upper()

    if sexo == "M":
        total_homens += 1
    elif sexo == "F" and idade < 20:
        total_mulheres_menores_20 += 1

    if idade > 18:
        total_pessoas_mais_18 += 1

    continue_input = input("Deseja continuar cadastrando pessoas? (S/N): ").strip().upper()
    if continue_input == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {total_pessoas_mais_18}")
print(f"Total de homens cadastrados: {total_homens}")
print(f"Total de mulheres com menos de 20 anos cadastradas: {total_mulheres_menores_20}")