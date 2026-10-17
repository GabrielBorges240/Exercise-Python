primo = int(input("Digite um número Primo:"))  
divisores = 0

for c in range(1, primo + 1):
    if primo % c == 0:
        divisores += 1 
        
if divisores == 2:
    print(f"{primo} é um número primo.")
else:
    print(f"{primo} não é um número primo.")     