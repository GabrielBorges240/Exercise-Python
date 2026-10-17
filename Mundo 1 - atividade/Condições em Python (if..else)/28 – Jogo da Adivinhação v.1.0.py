import random

aleatorio = random.randint(0, 5)
numero = int(input("Em que número eu pensei?")) 

if numero == aleatorio:
    print("Você venceu!")
else:
    print(f"Você errou! O número era:, {aleatorio}") 



 
