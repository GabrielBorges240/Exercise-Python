while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo in ["M", "F"]:
        break
    print("Sexo inválido. Digite M para masculino ou F para feminino.")

if sexo == "M":
    print("Você é do sexo masculino.")
elif sexo == "F":
    print("Você é do sexo feminino.")
else:
    print("Sexo inválido.")

 