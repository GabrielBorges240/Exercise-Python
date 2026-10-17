maior = menor = soma = 0
c = 1
continuar = 1
  
while continuar == 1:  # Exemplo: mostrar 10 termos
    numero = int(input(f"Digite um número: "))     
    soma += numero 
    if c == 1:
           maior = numero
           menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    c += 1
    
    continuar = int(input("Deseja continuar a digitar valores? [1] Sim [2] Não: "))

media = soma / (c - 1)
print(f"\033[1;32m Média dos valores: {media:.2f}\033[m")
print(f"\033[1;32mO maior número digitado foi: {maior}\033[m")  # sem \n aqui
print(f"\033[1;32mO menor número digitado foi: {menor}\033[m")
 
 
  
 
 