# -----------------------------
# CONDIÇÕES EM PYTHON (if / else)
# -----------------------------
# Estruturas condicionais permitem executar blocos de código
# dependendo de uma condição ser verdadeira ou falsa.

# -----------------------------
# CONDIÇÃO SIMPLES
# -----------------------------
# if - executa apenas se a condição for verdadeira
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("O número é PAR")

# -----------------------------
# CONDIÇÃO COMPOSTA
# -----------------------------
# if / else - executa um bloco se for verdadeiro, outro se for falso
n = int(input("Digite outro número: "))
if n % 2 == 0:
    print("O número é PAR")
else:
    print("O número é ÍMPAR")

# -----------------------------
# CONDIÇÃO ANINHADA
# -----------------------------
# if / elif / else - várias condições em sequência
nota = float(input("Digite sua nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# -----------------------------
# EXEMPLOS PRÁTICOS
# -----------------------------
# Verificar se a pessoa pode dirigir
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")

# -----------------------------
# EXERCÍCIOS DA AULA
# -----------------------------
# Ex. 28 → Faça um programa que leia a idade de uma pessoa e diga se ela é maior ou menor de idade.
# Ex. 29 → Crie um programa que leia dois números e mostre qual deles é maior.
# Ex. 30 → Desenvolva um programa que leia um número e diga se ele é par ou ímpar.
# Ex. 31 → Faça um programa que leia o ano de nascimento de uma pessoa e diga se ela pode votar.
# Ex. 32 → Crie um programa que leia um número inteiro e diga se ele é múltiplo de 2 ou de 3.
