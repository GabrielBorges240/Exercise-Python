# -----------------------------
# OPERADORES ARITMÉTICOS EM PYTHON
# -----------------------------
# +  adição
# -  subtração
# *  multiplicação
# /  divisão
# ** exponenciação (potência)
# // divisão inteira (quociente)
# %  módulo (resto da divisão)

# -----------------------------
# EXEMPLOS
# -----------------------------
print(5 + 2)   # 7 (adição)
print(5 - 2)   # 3 (subtração)
print(5 * 2)   # 10 (multiplicação)
print(5 / 2)   # 2.5 (divisão normal)
print(5 ** 2)  # 25 (potência: 5²)
print(5 // 2)  # 2 (divisão inteira)
print(5 % 2)   # 1 (resto da divisão)

# -----------------------------
# ORDEM DE PRECEDÊNCIA
# -----------------------------
# 1. Parênteses ()
# 2. Potência **
# 3. Multiplicação *, Divisão /, Divisão inteira //, Módulo %
# 4. Adição + e Subtração -

# Exemplo:
print(5 + 2 * 10)      # 25 (multiplicação antes da adição)
print((5 + 2) * 10)    # 70 (parênteses primeiro)

# -----------------------------
# EXERCÍCIOS DA AULA
# -----------------------------
# Ex. 5 → Faça um programa que mostre a soma entre dois números.
# Ex. 6 → Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
# Ex. 7 → Desenvolva um programa que leia as duas notas de um aluno e mostre a média.
# Ex. 8 → Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Ex. 9 → Faça um programa que leia um número inteiro e mostre sua tabuada.
# Ex. 10 → Crie um programa que leia um número real e mostre sua parte inteira.
# Ex. 11 → Faça um programa que leia a largura e altura de uma parede e calcule sua área e a quantidade de tinta necessária.
# Ex. 12 → Crie um programa que leia o preço de um produto e mostre seu novo preço com desconto.
# Ex. 13 → Faça um programa que leia o salário de um funcionário e mostre seu novo salário com aumento.


# ============================================================
# ORDEM DE PRECEDÊNCIA DOS OPERADORES EM PYTHON
# Baseado na Aula #07 (Operadores Aritméticos) - Curso em Vídeo
# ============================================================
#
# Ordem (do que é resolvido primeiro para o último):
#   1º  ( )              parênteses
#   2º  **               potência
#   3º  *  /  //  %      multiplicação, divisão, divisão inteira e resto
#   4º  +  -             adição e subtração
#
# Operadores do mesmo nível são resolvidos da ESQUERDA para a DIREITA
# (exceção: ** é resolvido da direita para a esquerda).
#
# Dica: antes de rodar cada linha, tente prever o resultado.


# ------------------------------------------------------------
# PARTE 1 - EXEMPLOS
# ------------------------------------------------------------
print("=== PARTE 1: EXEMPLOS ===")
print("5 + 3 * 2 =", 5 + 3 * 2)                        # 11   (* antes de +)
print("(5 + 3) * 2 =", (5 + 3) * 2)                    # 16   (parênteses primeiro)
print("2 * 3 ** 2 =", 2 * 3 ** 2)                      # 18   (3**2=9, depois 2*9)
print("(2 * 3) ** 2 =", (2 * 3) ** 2)                  # 36   (6**2)
print("10 - 4 + 2 =", 10 - 4 + 2)                      # 8    (esquerda p/ direita)
print("20 / 4 * 2 =", 20 / 4 * 2)                      # 10.0 (5.0 * 2)
print("20 // 3 * 3 =", 20 // 3 * 3)                    # 18   (6 * 3)
print("20 % 6 + 1 =", 20 % 6 + 1)                      # 3    (2 + 1)
print("10 + 20 % 3 ** 2 * 2 =", 10 + 20 % 3 ** 2 * 2)  # 14   (9 -> 20%9=2 -> 2*2=4 -> 10+4)
print("81 ** (1/2) =", 81 ** (1 / 2))                  # 9.0  (raiz quadrada)
print("-3 ** 2 =", -3 ** 2)                            # -9   (** antes do sinal)
print("(-3) ** 2 =", (-3) ** 2)                        # 9
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)                    # 512  (** vai da direita p/ esquerda: 3**2=9, 2**9)


# ------------------------------------------------------------
# PARTE 2 - EXERCÍCIOS RESOLVIDOS (prever antes de rodar)
# ------------------------------------------------------------
print("\n=== PARTE 2: EXERCÍCIOS ===")

# Ex 1
print("Ex 1:", 2 + 3 * 4)                     # 14
# Ex 2
print("Ex 2:", (2 + 3) * 4)                   # 20
# Ex 3
print("Ex 3:", 100 / 5 / 2)                   # 10.0  (20.0 / 2)
# Ex 4
print("Ex 4:", 17 // 5 + 17 % 5)              # 5     (3 + 2)
# Ex 5
print("Ex 5:", 10 + 5 * 2 ** 2 - 8 // 3)      # 28    (10 + 20 - 2)
# Ex 6
print("Ex 6:", (10 + 5) * 2 ** 2 - 8 // 3)    # 58    (15 * 4 - 2)
# Ex 7 - mesmo nível: esquerda para a direita
print("Ex 7:", 7 * 3 % 5)                     # 1     ((7*3) % 5 = 21 % 5)
# Ex 8 - o mesmo cálculo com parênteses muda o resultado
print("Ex 8:", 7 * (3 % 5))                   # 21    (7 * 3)


# ------------------------------------------------------------
# PARTE 3 - PROBLEMAS PRÁTICOS RESOLVIDOS
# (troque os valores fixos por input() se quiser testar outros)
# ------------------------------------------------------------
print("\n=== PARTE 3: PROBLEMAS PRÁTICOS ===")

# Ex 9 - Média de duas notas (parênteses são obrigatórios!)
n1 = 7.5
n2 = 8.5
errada = n1 + n2 / 2        # 11.75 -> só o n2 é dividido
certa = (n1 + n2) / 2       # 8.0
print(f"Ex 9: sem parênteses = {errada} | com parênteses = {certa}")

# Ex 10 - Converter segundos em minutos e segundos (// e %)
total = 135
minutos = total // 60       # 2
segundos = total % 60       # 15
print(f"Ex 10: {total} segundos = {minutos} min e {segundos} s")

# Ex 11 - Par ou ímpar (% e condição)
numero = 7
print(f"Ex 11: {numero} % 2 = {numero % 2}")   # 1
if numero % 2 == 0:
    print(f"Ex 11: {numero} é par")
else:
    print(f"Ex 11: {numero} é ímpar")

# Ex 12 - Cédulas de 50, 10 e 1 para um valor (// e %)
valor = 187
notas50 = valor // 50       # 3
resto = valor % 50          # 37
notas10 = resto // 10       # 3
resto = resto % 10          # 7
notas1 = resto              # 7
print(f"Ex 12: {valor} = {notas50}x50 + {notas10}x10 + {notas1}x1")

# Ex 13 - Operadores de atribuição composta (+=, -=, *=, //=, **=, %=)
x = 10
x += 5                      # x = x + 5   -> 15
print("Ex 13: += 5   ->", x)
x -= 3                      # x = x - 3   -> 12
print("Ex 13: -= 3   ->", x)
x *= 2                      # x = x * 2   -> 24
print("Ex 13: *= 2   ->", x)
x //= 5                     # x = x // 5  -> 4
print("Ex 13: //= 5  ->", x)
x **= 3                     # x = x ** 3  -> 64
print("Ex 13: **= 3  ->", x)
x %= 10                     # x = x % 10  -> 4
print("Ex 13: %= 10  ->", x)