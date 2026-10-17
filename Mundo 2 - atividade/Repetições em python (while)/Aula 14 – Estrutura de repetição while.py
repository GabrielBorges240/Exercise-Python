"""
==========================================================
AULA 14 - ESTRUTURA DE REPETIÇÃO WHILE
==========================================================

O que é o while?
-----------------
O "while" (traduzindo: "enquanto") é uma estrutura de repetição
(laço/loop) que executa um bloco de código ENQUANTO uma condição
for verdadeira (True).

Sintaxe básica:

    while condicao:
        # bloco de código que se repete
        # (precisa ter algo que, eventualmente, torne a condição falsa)

Diferença entre while e for:
- for: usado quando SABEMOS quantas vezes o laço vai repetir
       (ex: percorrer uma lista, repetir 10 vezes)
- while: usado quando NÃO sabemos exatamente quantas vezes vai
         repetir, e a repetição depende de uma condição (ex:
         repetir até o usuário digitar "sair")

CUIDADO: Se a condição nunca se tornar falsa, o laço vira um
"loop infinito" e o programa nunca para! Por isso é essencial
sempre ter, dentro do while, algo que altere a variável usada
na condição (como um contador sendo incrementado).
==========================================================
"""

# ----------------------------------------------------------
# EXEMPLO 1 - O exemplo da aula (corrigido e comentado)
# ----------------------------------------------------------

# Aqui está o código da aula, com a sintaxe correta do Python.
# Observação importante: em Python, depois do "while condicao"
# é OBRIGATÓRIO colocar dois pontos ( : ), e o bloco de dentro
# do while precisa estar indentado (com espaços/tab).

c = 1                  # variável contadora, começa em 1
while c != 10:          # repete enquanto c for diferente de 10
    print(c)            # mostra o valor atual de c
    c += 1               # incrementa c em 1 (equivale a c = c + 1)
                        # -> sem essa linha, o laço seria infinito!

print('Acabou')        # executado depois que o while terminar
# Saída: 1 2 3 4 5 6 7 8 9  e depois "Acabou"


# ----------------------------------------------------------
# EXEMPLO 2 - Contagem regressiva
# ----------------------------------------------------------

print("\n--- Exemplo 2: contagem regressiva ---")

numero = 5
while numero > 0:          # repete enquanto numero for maior que 0
    print(numero)
    numero -= 1              # decrementa 1 a cada repetição
print("Fogo!")              # aparece quando numero chega a 0


# ----------------------------------------------------------
# EXEMPLO 3 - while com entrada do usuário (input)
# ----------------------------------------------------------

print("\n--- Exemplo 3: repetir até digitar 'sair' ---")

palavra = ""                        # variável começa vazia
while palavra != "sair":
    palavra = input("Digite algo (ou 'sair' para encerrar): ")
    print(f"Você digitou: {palavra}")
print("Programa encerrado.")


# ----------------------------------------------------------
# EXEMPLO 4 - while True + break (parada controlada por condição interna)
# ----------------------------------------------------------

print("\n--- Exemplo 4: while True com break ---")

contador = 0
while True:              # "while True" repete para sempre...
    print("Rodando...", contador)
    contador += 1
    if contador == 3:     # ...até encontrarmos um break
        print("Chegou a 3, saindo do laço com break!")
        break            # break interrompe o laço imediatamente


"""
==========================================================
EXERCÍCIOS RESOLVIDOS
==========================================================
"""

# ----------------------------------------------------------
# EXERCÍCIO 1
# Enunciado: Faça um programa que imprima os números de 1 até 20
# usando while.
# ----------------------------------------------------------

print("\n--- Exercício 1 ---")

n = 1                       # inicia o contador em 1
while n <= 20:               # continua enquanto n for menor ou igual a 20
    print(n)
    n += 1                   # incrementa para não travar em loop infinito


# ----------------------------------------------------------
# EXERCÍCIO 2
# Enunciado: Faça um programa que peça um número ao usuário e
# mostre a tabuada desse número (de 1 a 10).
# ----------------------------------------------------------

print("\n--- Exercício 2 ---")

# num = int(input("Digite um número para ver a tabuada: "))
num = 7                      # valor fixo aqui só para teste automático
                             # (na prática, use a linha do input acima)

i = 1                        # contador que vai de 1 até 10
while i <= 10:
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    i += 1


# ----------------------------------------------------------
# EXERCÍCIO 3
# Enunciado: Faça um programa que some os números de 1 até 100
# e mostre o resultado da soma (sem usar a fórmula matemática,
# usando while para ir somando um por um).
# ----------------------------------------------------------

print("\n--- Exercício 3 ---")

soma = 0                     # acumulador, começa zerado
num_atual = 1                # contador começa em 1
while num_atual <= 100:
    soma += num_atual         # soma = soma + num_atual
    num_atual += 1
print(f"A soma de 1 até 100 é: {soma}")


# ----------------------------------------------------------
# EXERCÍCIO 4
# Enunciado: Faça um programa que peça uma senha ao usuário e
# só libere o acesso quando ele digitar a senha correta.
# ----------------------------------------------------------

print("\n--- Exercício 4 ---")

SENHA_CORRETA = "python123"
# senha_digitada = ""
# while senha_digitada != SENHA_CORRETA:
#     senha_digitada = input("Digite a senha: ")
#     if senha_digitada != SENHA_CORRETA:
#         print("Senha incorreta, tente novamente.")
# print("Acesso liberado!")

# (código acima comentado para não travar a execução automática
#  do arquivo; descomente as linhas para testar interativamente)


# ----------------------------------------------------------
# EXERCÍCIO 5
# Enunciado: Faça um programa que conte quantos números pares
# existem entre 1 e 50, usando while.
# ----------------------------------------------------------

print("\n--- Exercício 5 ---")

numero_atual = 1
quantidade_pares = 0
while numero_atual <= 50:
    if numero_atual % 2 == 0:       # resto da divisão por 2 igual a 0 = par
        quantidade_pares += 1
    numero_atual += 1
print(f"Quantidade de números pares entre 1 e 50: {quantidade_pares}")

"""
==========================================================
DICAS FINAIS
==========================================================
1. Sempre confira se a variável usada na condição do while
   está sendo alterada dentro do laço (senão: loop infinito).
2. "while True" + "break" é útil quando a condição de parada
   depende de algo que só é verificado no meio do laço.
3. "continue" pode ser usado para pular para a próxima repetição
   sem executar o restante do bloco naquela volta.
4. Teste sempre com valores pequenos primeiro, para garantir
   que a lógica está correta antes de rodar com números grandes.
==========================================================
"""