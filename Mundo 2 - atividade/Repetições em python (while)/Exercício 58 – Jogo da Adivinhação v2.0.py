import random

aleatório = random.randint(0, 5)
número = int(input("Em que número eu pensei? ")) 

tentativas = 1

while número != aleatório:
    número = int(input("Tente novamente: "))
    tentativas += 1
    
print("\033[1;32mParabéns! Você acertou.\033[m") 
print(f"Quantidade de palpites: {tentativas}")
print(f"O número que eu pensei foi: {aleatório}.")

 