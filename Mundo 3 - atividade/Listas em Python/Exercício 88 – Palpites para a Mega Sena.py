import random

lista = []

quantidade = int(input("Quantos jogos você quer que eu sorteie? "))

for _ in range(quantidade):
    jogo = sorted(random.sample(range(1, 61), 6))
    lista.append(jogo)

for i, jogo in enumerate(lista, 1):
    print(f"Jogo {i}: {jogo}")
