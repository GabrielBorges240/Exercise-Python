# =============================================================
# AULA: LAÇOS DE REPETIÇÃO - FOR
# =============================================================
#
# O "for" é uma estrutura de repetição (laço/loop) usada quando
# JÁ SABEMOS quantas vezes queremos repetir um bloco de código,
# ou quando queremos percorrer todos os itens de uma sequência
# (lista, string, range, tupla, etc).
#
# Diferente do "while" (que repete enquanto uma condição for
# verdadeira), o "for" percorre item por item de algo iterável.


# -------------------------------------------------------------
# 1) A FUNÇÃO range()
# -------------------------------------------------------------
# range() gera uma sequência de números inteiros.
# Sintaxe: range(início, fim, passo)
#
# IMPORTANTE: o valor "fim" NUNCA é incluído no resultado.
# range(0, 4) gera: 0, 1, 2, 3  (o 4 NÃO entra)

print("Exemplo 1: range(0, 4)")
for c in range(0, 4):
    print(c)
print("Acabou")
print()  # linha em branco só pra separar os exemplos


# -------------------------------------------------------------
# 2) range() COM APENAS UM PARÂMETRO
# -------------------------------------------------------------
# Quando passamos só um número, o Python entende que é o "fim",
# e o início é automaticamente 0.
# range(4) é o mesmo que range(0, 4)

print("Exemplo 2: range(4) -> começa do 0 automaticamente")
for c in range(4):
    print(c)
print("Acabou")
print()


# -------------------------------------------------------------
# 3) range() COM PASSO (STEP)
# -------------------------------------------------------------
# O terceiro parâmetro define de quanto em quanto os números
# vão "pular". Por padrão o passo é 1.

print("Exemplo 3: range(0, 10, 2) -> de 2 em 2")
for c in range(0, 10, 2):
    print(c)
print("Acabou")
print()


# -------------------------------------------------------------
# 4) range() REGRESSIVO (contando pra trás)
# -------------------------------------------------------------
# Para contar de trás pra frente, o passo precisa ser NEGATIVO,
# e o início deve ser maior que o fim.

print("Exemplo 4: contagem regressiva de 5 até 1")
for c in range(5, 0, -1):
    print(c)
print("Lançamento!")
print()


# -------------------------------------------------------------
# 5) FOR PERCORRENDO UMA STRING
# -------------------------------------------------------------
# O "for" também funciona em strings, percorrendo caractere
# por caractere.

print("Exemplo 5: percorrendo uma palavra")
palavra = "Python"
for letra in palavra:
    print(letra)
print()


# -------------------------------------------------------------
# 6) FOR PERCORRENDO UMA LISTA
# -------------------------------------------------------------
# Muito usado no dia a dia: percorrer os elementos de uma lista
# um por um, sem precisar controlar índice manualmente.

print("Exemplo 6: percorrendo uma lista")
frutas = ["Maçã", "Banana", "Laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
print()


# -------------------------------------------------------------
# 7) USANDO O FOR PARA SOMAR/CONTAR (ACUMULADOR)
# -------------------------------------------------------------
# Um padrão muito comum: criar uma variável "acumuladora" antes
# do laço, e ir somando/alterando ela a cada volta (iteração).

print("Exemplo 7: somando números de 1 a 5")
soma = 0  # começa zerado, fora do laço
for numero in range(1, 6):  # 1, 2, 3, 4, 5
    soma = soma + numero    # a cada volta, soma o número atual
print(f"A soma total é: {soma}")
print()


# -------------------------------------------------------------
# 8) FOR COM CONDIÇÃO DENTRO (if dentro do for)
# -------------------------------------------------------------
# É muito comum combinar for + if para filtrar valores.

print("Exemplo 8: mostrando só os números pares de 0 a 9")
for n in range(10):
    if n % 2 == 0:  # resto da divisão por 2 igual a 0 = par
        print(f"{n} é par")
print()


# -------------------------------------------------------------
# 9) FOR ANINHADO (um for dentro do outro)
# -------------------------------------------------------------
# Útil para tabelas, matrizes, tabuada, etc.

print("Exemplo 9: tabuada do 1 ao 3")
for tabuada in range(1, 4):        # for de fora: 1, 2, 3
    for multiplicador in range(1, 4):  # for de dentro: 1, 2, 3
        resultado = tabuada * multiplicador
        print(f"{tabuada} x {multiplicador} = {resultado}")
    print("---")  # separa cada tabuada
print()


# -------------------------------------------------------------
# RESUMO RÁPIDO
# -------------------------------------------------------------
# for variavel in sequencia:
#     bloco de código (repete uma vez para cada item)
#
# - range(fim)              -> começa em 0, vai até fim-1
# - range(inicio, fim)      -> vai de inicio até fim-1
# - range(inicio, fim, pas) -> pula de "pas" em "pas"
# - também funciona em strings, listas, tuplas etc.