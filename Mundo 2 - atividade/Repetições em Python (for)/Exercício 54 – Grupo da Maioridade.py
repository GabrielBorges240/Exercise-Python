from datetime import date

ano_atual = date.today().year
maioridade = 0
menoridade = 0  

for c in range(1, 8):
    ano_nascimento = int(input(f"em que ano a {c}° pessoa nasceu? "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f"ao todo tivemos {maioridade} pessoas maiores de idade.")
print(f"e também tivemos {menoridade} pessoas menores de idade.")



