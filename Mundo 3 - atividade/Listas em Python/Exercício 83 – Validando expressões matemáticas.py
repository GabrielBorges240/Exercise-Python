lista = []
expression = input("Digite uma expressão matemática:")

for caractere in expression:
    if caractere == "(":
        lista.append(caractere)
    elif caractere == ")":
        if len(lista) == 0:
            lista.append(caractere)
            break
        lista.pop()

if len(lista) == 0:
    print(f"A expressão:{expression} é válida.")
else:
    print(f"A expressão:{expression} não é válida.")