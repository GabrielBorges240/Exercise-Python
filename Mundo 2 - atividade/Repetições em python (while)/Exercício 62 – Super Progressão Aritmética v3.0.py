Termo = int(input("Primeiro termo: "))
Razao = int(input("Razão: "))
Termos = int(input("Quantos termos você quer mostrar? "))

contador = 1
total = 0 

while Termos != 0:   # aqui o controle fica mais claro
    total += Termos
    while contador <= total:
        print(f"\033[1;32m{Termo} → \033[m", end="")
        contador += 1
        Termo += Razao
    print("\033[1;32mPAUSA\033[m")
    Termos = int(input("Quantos termos você quer mostrar a mais? "))
print(f"\033[1;32mProgressão finalizada com {total} termos mostrados.\033[m")
