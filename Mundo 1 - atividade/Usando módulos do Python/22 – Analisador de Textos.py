nome = (input("Digite seu nome completo:")).strip()

print("Nome em maiúsculas:", nome.upper())
print("Nome em minúsculas:", nome.lower())
print("Quantidade de letras (sem espaços):", len(nome) - nome.count(" "))
print("Quantidade de letras do primeiro nome:", len(nome.split()[0]))




 