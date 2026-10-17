Termo = int(input("Primeiro Termo:"))  
Razao = int(input("Razão:"))

contador = 1

while contador <= 10:
    print(f"\033[1;32m{Termo} → \033[m", end="")
    contador += 1
    Termo += Razao
print("\033[1;32mAcabou\033[m")
 