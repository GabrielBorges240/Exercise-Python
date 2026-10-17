soma = 0
contador = 0

while True:  # Exemplo: mostrar 10 termo
    numero = int(input("Digite um número:"))  
    print(f"\033[1;32m{numero} → \033[m", end="")
    if numero == 999:
        break
    soma += numero
    contador += 1
   
print(f"Foram digitados {contador} números e a soma entre eles é {soma}.")