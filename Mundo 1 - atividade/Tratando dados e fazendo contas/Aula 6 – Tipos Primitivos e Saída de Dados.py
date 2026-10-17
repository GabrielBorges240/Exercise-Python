# -----------------------------
# TIPOS PRIMITIVOS EM PYTHON
# -----------------------------
# int   → números inteiros (ex: 7, -4, 0, 9875)
# float → números reais (ex: 4.5, 0.076, -15.223)
# bool  → valores lógicos (True ou False)
# str   → textos, cadeias de caracteres (ex: "Olá", 'Python')

# -----------------------------
# ENTRADA DE DADOS
# -----------------------------
# input() - lê dados do teclado sempre como string
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("Olá", nome, "você tem", idade, "anos.")

# -----------------------------
# CONVERSÃO DE TIPOS
# -----------------------------
# int()   - converte para inteiro
# float() - converte para real
# str()   - converte para string
# bool()  - converte para lógico

n1 = int(input("Digite um número inteiro: "))
n2 = float(input("Digite um número real: "))
print("Soma =", n1 + n2)

# -----------------------------
# SAÍDA DE DADOS
# -----------------------------
# print() - mostra informações na tela
# Pode usar vírgulas ou formatação

# Exemplo com vírgulas
print("O número digitado foi", n1)

# Exemplo com format()
print("O número digitado foi {}".format(n1))

# Exemplo com f-string (Python 3.6+)
print(f"O número digitado foi {n1}")

# -----------------------------
# OPERAÇÕES COM PRINT()
# -----------------------------
# Podemos combinar texto e cálculos diretamente
n3 = int(input("Digite outro número: "))
print("O dobro de {} é {}".format(n3, n3*2))
print(f"O triplo de {n3} é {n3*3}")
print("A raiz quadrada de {} é {:.2f}".format(n3, n3**0.5))

# -----------------------------
# EXERCÍCIOS DA AULA
# -----------------------------
# Ex. 3 → Crie um programa que leia dois números e mostre a soma entre eles.
# Ex. 4 → Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações possíveis sobre ele.
