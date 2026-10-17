numero = int(input("Digite um número:"))  

t1 = 0
t2 = 1
contador = 3
print(f"{t1} → {t2} → ", end="")

while contador <= numero:
    t3 = t1 + t2
    print(f"\033[1;32m{t3} → \033[m", end="")
    t1 = t2
    t2 = t3
    contador += 1
print("\033[1;32mAcabou\033[m")
 