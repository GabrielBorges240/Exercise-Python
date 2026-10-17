numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite o segundo numero:"))
numero3 = int(input("Digite terceiro numero:"))

menor = numero1 
maior = numero1 

if numero2 > maior:
    maior = numero2
if numero3 >  maior:
    maior  = numero3     

if numero2 < menor:
    menor = numero2
if numero3 <  menor :
    menor  = numero3       

print(f'maior numero {maior}')      
print(f'menor numero {menor}')       