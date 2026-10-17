original = input("Digite uma frase:")

frase = original.replace(" ", "").lower()
inverso = frase[::-1]

if frase == inverso:
    print(f"{frase} é um palíndromo.")
else:
    print(f"{frase} não é um palíndromo.")