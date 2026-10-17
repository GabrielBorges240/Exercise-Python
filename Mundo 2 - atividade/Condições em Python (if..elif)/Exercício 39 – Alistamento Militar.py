from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))
sexo = input("Digite o sexo (M/F): ").strip().upper()
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual} ")

if sexo == "M":
    if idade == 18:
        print("Você deve se alistar imediatamente!")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Você ainda não tem 18 anos. Faltam {saldo} anos para o alistamento.")
        print(f"Seu alistamento será em {ano_atual + saldo}.")
    else:
        saldo = idade - 18
        print(f"Você já deveria ter se alistado há {saldo} anos.")
        print(f"Seu alistamento foi em {ano_atual - saldo}.")

elif sexo == "F":
     
    if idade == 18:
        print("Mulheres não são obrigadas a se alistar.")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Mulheres não são obrigadas a se alistar. Faltam {saldo} anos para completar 18 anos.")
        print(f"Ano em que fará 18: {ano_atual + saldo}.")
    else:
        saldo = idade - 18
        print(f"Mulheres não são obrigadas a se alistar. Já se passaram {saldo} anos desde que completar 18.")
        print(f"Ano em que completou 18: {ano_atual - saldo}.")

else:
    print("Sexo inválido. Use 'M' ou 'F'.")
