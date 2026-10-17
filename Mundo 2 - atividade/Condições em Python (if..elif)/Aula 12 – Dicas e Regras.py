# ============================================================
# ESTRUTURAS DE CONTROLE EM PYTHON
# if / elif / else | for | while
# ============================================================
# Estruturas de controle são comandos que alteram a ordem
# "normal" de execução do código (que é de cima para baixo,
# linha por linha). Elas permitem:
#   - Tomar decisões (if/elif/else)
#   - Repetir blocos de código (for, while)
# ============================================================


# ------------------------------------------------------------
# 1) IF / ELIF / ELSE — ESTRUTURA CONDICIONAL
# ------------------------------------------------------------
# Serve para executar um bloco de código APENAS SE uma condição
# for verdadeira (True). Podemos encadear várias condições com
# "elif" (senão, se...) e finalizar com um "else" (senão) que
# cobre todos os outros casos.
#
# Sintaxe:
#   if condicao1:
#       # executa se condicao1 for True
#   elif condicao2:
#       # executa se condicao1 for False e condicao2 for True
#   else:
#       # executa se nenhuma condição acima for True
#
# IMPORTANTE: em Python, a indentação (espaços no início da
# linha) define o que pertence a cada bloco. Não existem chaves {}.

idade = int(input("Qual sua idade? "))

if idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")

# Dica: o "elif" só é avaliado se o "if" anterior for falso.
# Você pode ter quantos "elif" quiser, mas só um "if" e um "else".


# ------------------------------------------------------------
# 2) FOR — ESTRUTURA DE REPETIÇÃO COM NÚMERO DEFINIDO DE VEZES
# ------------------------------------------------------------
# O "for" percorre uma sequência (lista, string, range, etc.)
# e repete o bloco de código uma vez para cada item dessa
# sequência. É ideal quando você SABE quantas vezes quer repetir
# ou tem uma coleção de itens para processar.
#
# Sintaxe:
#   for variavel in sequencia:
#       # bloco repetido para cada item

# Exemplo 1: usando range() para contar de 1 até 5
for numero in range(1, 6):  # 6 é o limite, mas NÃO é incluído
    print(f"Contando: {numero}")

# Exemplo 2: percorrendo uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

# Exemplo 3: percorrendo os caracteres de uma string
for letra in "Python":
    print(letra)


# ------------------------------------------------------------
# 3) WHILE — ESTRUTURA DE REPETIÇÃO COM CONDIÇÃO
# ------------------------------------------------------------
# O "while" repete um bloco de código ENQUANTO uma condição for
# verdadeira. É ideal quando você NÃO SABE de antemão quantas
# vezes o código vai repetir — a repetição depende de uma
# condição que pode mudar durante a execução.
#
# Sintaxe:
#   while condicao:
#       # bloco repetido enquanto condicao for True
#
# CUIDADO: se a condição nunca se tornar False, o código entra
# em um "loop infinito" e trava o programa. Sempre garanta que
# algo dentro do while, eventualmente, torne a condição falsa.

contador = 1
while contador <= 5:
    print(f"Repetição número {contador}")
    contador += 1  # incrementa o contador; sem isso o loop nunca acaba

# Exemplo prático: validar entrada do usuário até ele digitar
# um valor correto (loop controlado por condição, não por contagem)
senha = ""
while senha != "1234":
    senha = input("Digite a senha (1234): ")
print("Senha correta! Acesso liberado.")


# ------------------------------------------------------------
# RESUMO — QUANDO USAR CADA UM?
# ------------------------------------------------------------
# if/elif/else -> quando você precisa tomar uma decisão baseada
#                 em uma ou mais condições.
#
# for           -> quando você sabe quantas vezes quer repetir,
#                 ou quer percorrer uma coleção (lista, string,
#                 range, dicionário, etc.).
#
# while         -> quando a repetição depende de uma condição
#                 que só é conhecida durante a execução (ex:
#                 repetir "até o usuário acertar" ou "até o
#                 saldo acabar").
# ------------------------------------------------------------