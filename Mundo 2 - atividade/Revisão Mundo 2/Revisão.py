"""
=============================================================
REVISAO - MUNDO 2 (Curso em Video, Gustavo Guanabara)
Condicoes (if/elif) | Repeticao for | Repeticao while
Com exemplos comentados para cada topico
=============================================================
"""

# =============================================================
# 1) CONDICOES EM PYTHON (if / elif / else)
# =============================================================
#
# Estrutura basica:
# if condicao:
#     bloco executado se a condicao for True
# elif outra_condicao:
#     so eh testado se a condicao acima foi False
# else:
#     executa se nenhuma condicao anterior foi True
#
# - A indentacao (4 espacos) eh o que define o que esta "dentro" do if
# - Relacionais: == != > < >= <=
# - Logicos: and / or / not
# - Cuidado: usar '=' no lugar de '==' ja gera erro de sintaxe no if
#
# Traducao livre das palavras-chave:
#   if    -> "se"
#   elif  -> "senao, se" (junção de else + if -> "senao se outra condicao")
#   else  -> "senao" (NAO eh "nao")
#
# Logica em portugues: "SE isso, SENAO SE aquilo, SENAO (nada disso) faca isso outro"
# O elif so eh testado quando o if anterior deu falso;
# o else so roda quando nenhuma condicao acima foi verdadeira.

# Exemplo simples:
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
# -> "Adulto" (porque 20 nao eh < 18, mas eh < 60)


# --- Exercicio 36 - Aprovando Emprestimo -----------------------
# Tema: if/elif com varias faixas de valor
salario = 2500
valor_imovel = 200000
prestacao_maxima = salario * 0.3          # 30% do salario
prestacao = valor_imovel / 200            # exemplo: financiado em 200x
if prestacao <= prestacao_maxima:
    print(f"Emprestimo aprovado. Prestacao: R$ {prestacao:.2f}")
else:
    print(f"Emprestimo negado. Prestacao seria R$ {prestacao:.2f}, "
          f"acima do limite de R$ {prestacao_maxima:.2f}")


# --- Exercicio 37 - Conversor de Bases Numericas ----------------
# Tema: menu com if/elif + funcoes bin(), oct(), hex()
numero = 25
opcao = 'B'  # simulando escolha do usuario
if opcao == 'B':
    print(f"{numero} em binario: {bin(numero)[2:]}")   # [2:] remove o prefixo "0b"
elif opcao == 'O':
    print(f"{numero} em octal: {oct(numero)[2:]}")     # remove "0o"
elif opcao == 'H':
    print(f"{numero} em hexadecimal: {hex(numero)[2:]}")  # remove "0x"


# --- Exercicio 38 - Comparando numeros ---------------------------
# Tema: comparar 3 valores com if aninhado
a, b, c = 4, 9, 2
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c
print(f"O maior valor eh {maior}")


# --- Exercicio 39 - Alistamento Militar ---------------------------
# Tema: idade = ano_atual - ano_nascimento, depois condicao
from datetime import datetime
ano_nascimento = 2008
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
if idade == 18:
    print("Voce deve se alistar este ano")
elif idade < 18:
    print(f"Ainda falta(m) {18 - idade} ano(s) para se alistar")
else:
    print(f"Voce ja passou {idade - 18} ano(s) da idade de alistamento")


# --- Exercicio 40 - Aquele classico da Media -----------------------
# Tema: media ponderada + faixas de conceito
nota1, nota2 = 7.0, 8.5
media = (nota1 * 3 + nota2 * 7) / 10   # media ponderada (pesos 3 e 7)
if media >= 9:
    conceito = 'A'
elif media >= 7:
    conceito = 'B'
elif media >= 5:
    conceito = 'C'
else:
    conceito = 'D'
print(f"Media {media:.1f} -> Conceito {conceito}")


# --- Exercicio 41 - Classificando Atletas ---------------------------
# Tema: IMC + faixa etaria, combinando and / or
peso, altura, idade_atleta = 70, 1.75, 22
imc = peso / altura ** 2
if imc < 18.5 or idade_atleta < 18:
    print("Nao apto")
else:
    print("Apto")


# --- Exercicio 42 - Analisando Triangulos -----------------------------
# Tema: existencia de triangulo (soma de 2 lados > o terceiro) e tipo
r1, r2, r3 = 5, 5, 5
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print("Equilatero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("Nao forma triangulo")


# --- Exercicio 43 - Indice de Massa Corporal -----------------------------
# Tema: formula imc = peso / altura**2 + faixas
peso, altura = 65, 1.70
imc = peso / altura ** 2
if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc < 25:
    situacao = "Peso ideal"
elif imc < 30:
    situacao = "Sobrepeso"
else:
    situacao = "Obesidade"
print(f"IMC {imc:.1f} -> {situacao}")


# --- Exercicio 44 - Gerenciador de Pagamento -------------------------------
# Tema: if/elif com desconto por forma de pagamento
preco = 100
forma = "avista"
if forma == "avista":
    preco *= 0.90       # 10% de desconto
elif forma == "cartao_1x":
    preco *= 0.95       # 5% de desconto
elif forma == "cartao_2x_mais":
    preco *= 1.20       # 20% de acrescimo
print(f"Preco final: R$ {preco:.2f}")


# --- Exercicio 45 - GAME Pedra Papel e Tesoura -------------------------------
# Tema: matriz de decisao jogador x computador
import random
jogador = "pedra"
computador = random.choice(["pedra", "papel", "tesoura"])
if jogador == computador:
    resultado = "Empate"
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    resultado = "Jogador venceu"
else:
    resultado = "Computador venceu"
print(f"Voce: {jogador} | PC: {computador} -> {resultado}")

# ATENCAO neste bloco:
# - ordenar os elif do mais especifico para o mais generico
# - evitar condicoes redundantes
# - lembrar do curto-circuito em and/or (o segundo lado nem sempre eh avaliado)


# =============================================================
# 2) REPETICAO COM for
# =============================================================
#
# for variavel in range(inicio, fim, passo):
#     bloco repetido
#
# - range(fim)                -> vai de 0 ate fim-1
# - range(inicio, fim)        -> vai de inicio ate fim-1
# - range(inicio, fim, passo) -> passo pode ser negativo (regressiva)
# - for item in lista: itera direto sobre sequencias (listas, strings...)
# - break interrompe o laco; continue pula para a proxima iteracao
# - padrao de acumulador: soma = 0 antes do loop, soma += valor dentro dele

# Exemplo simples:
for i in range(1, 6):
    print(i, end=" ")
# -> 1 2 3 4 5


# --- Exercicio 46 - Contagem regressiva -----------------------
# Tema: range com passo negativo
for i in range(10, 0, -1):
    print(i, end=" ")
print("Fogo!")


# --- Exercicio 47 - Contagem de pares ---------------------------
# Tema: range com passo 2 (ou checagem com %)
for i in range(0, 21, 2):
    print(i, end=" ")


# --- Exercicio 48 - Soma de impares multiplos de 3 --------------------
# Tema: filtro dentro do for + acumulador
soma = 0
for n in range(1, 100, 2):          # so numeros impares
    if n % 3 == 0:                  # que tambem sao multiplos de 3
        soma += n
print(f"Soma: {soma}")


# --- Exercicio 49 - Tabuada v2.0 ---------------------------------
# Tema: for de 1 a 10, formatacao de saida
numero = 7
for i in range(1, 11):
    print(f"{numero} x {i:2} = {numero * i}")


# --- Exercicio 50 - Soma dos pares ---------------------------------
# Tema: acumulador condicional
valores = [4, 7, 10, 3, 8]
soma_pares = 0
for v in valores:
    if v % 2 == 0:
        soma_pares += v
print(f"Soma dos pares: {soma_pares}")


# --- Exercicio 51 - Progressao Aritmetica -----------------------------
# Tema: formula do termo geral ou acumulador com for
primeiro_termo, razao, qtd_termos = 2, 3, 10
for n in range(qtd_termos):
    termo = primeiro_termo + n * razao   # formula: a_n = a1 + (n-1)*r
    print(termo, end=" ")


# --- Exercicio 52 - Numeros primos ---------------------------------------
# Tema: checagem de divisores dentro de outro for (laco aninhado)
numero = 29
primo = True
if numero < 2:
    primo = False
else:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break               # ja achou divisor, nao precisa continuar
print(f"{numero} e primo? {primo}")


# --- Exercicio 53 - Detector de Palindromo ---------------------------------
# Tema: comparar string com sua reversa
palavra = "arara"
limpa = palavra.strip().upper()
if limpa == limpa[::-1]:        # [::-1] inverte a string
    print("E palindromo")
else:
    print("Nao e palindromo")


# --- Exercicio 54 - Grupo da Maioridade ---------------------------------------
# Tema: contar quantos sao maiores/menores de idade numa lista
idades = [15, 22, 17, 30, 12, 40]
maiores = 0
menores = 0
for idade in idades:
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f"Maiores: {maiores} | Menores: {menores}")


# --- Exercicio 55 - Maior e menor da sequencia -----------------------------------
# Tema: variaveis maior/menor atualizadas a cada iteracao
numeros = [5, 9, 2, 8, 1]
maior = menores_valor = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
    if n < menores_valor:
        menores_valor = n
print(f"Maior: {maior} | Menor: {menores_valor}")


# --- Exercicio 56 - Analisador completo -------------------------------------------
# Tema: combina varias tecnicas anteriores num so programa
lista = []
for i in range(1, 6):
    lista.append(i * 2)         # simula 5 "cadastros"
print(f"Lista: {lista}")
print(f"Maior: {max(lista)} | Menor: {min(lista)} | Soma: {sum(lista)}")

# ATENCAO neste bloco:
# - cuidado com off-by-one em range() (ele nao inclui o valor final)
# - em lacos aninhados (ex: numeros primos), use break para nao rodar a toa


# =============================================================
# 3) REPETICAO COM while
# =============================================================
#
# while condicao:
#     bloco repetido enquanto condicao for True
#
# - diferente do for, o while NAO tem fim automatico:
#   a condicao de parada precisa mudar dentro do loop, senao vira infinito
# - "while True:" + "break" e um padrao comum: repete ate o usuario decidir sair
# - f-strings (f"texto {variavel}") ajudam a formatar a saida

# Exemplo simples:
contador = 0
while contador < 5:
    print(contador, end=" ")
    contador += 1        # ESSENCIAL: sem isso, loop infinito
# -> 0 1 2 3 4


# --- Exercicio 57 - Validacao de Dados -----------------------
# Tema: while repetindo ate a entrada ser valida
valor_simulado = [-5, -1, 8]   # simula tentativas de "input"
i = 0
numero = valor_simulado[i]
while numero < 0:
    i += 1
    numero = valor_simulado[i]   # em codigo real seria: int(input("Digite: "))
print(f"Valor valido: {numero}")


# --- Exercicio 58 - Jogo da Adivinhacao v2.0 --------------------
# Tema: while + random.randint, contagem de tentativas
import random
numero_secreto = random.randint(1, 10)
tentativas = 0
chute = 7   # simula o chute do usuario
while chute != numero_secreto:
    tentativas += 1
    # em codigo real: chute = int(input("Chute: "))
    break   # (aqui so pra nao rodar infinito no exemplo)
print(f"Tentativas: {tentativas}")


# --- Exercicio 59 - Criando um Menu --------------------------------
# Tema: while True com menu e break na opcao de sair
opcoes_simuladas = ["1", "2", "5"]  # simula escolhas do usuario
for opcao in opcoes_simuladas:      # substitui o input() real no exemplo
    if opcao == "1":
        print("Opcao 1 executada")
    elif opcao == "2":
        print("Opcao 2 executada")
    elif opcao == "5":
        print("Saindo...")
        break


# --- Exercicio 60 - Calculo do Fatorial ----------------------------
# Tema: acumulador multiplicativo (fat *= n)
numero = 5
fatorial = 1
n = numero
while n > 1:
    fatorial *= n
    n -= 1
print(f"{numero}! = {fatorial}")


# --- Exercicio 61 - Progressao Aritmetica (while) ------------------------
# Tema: mesmo tema do ex. 51, agora controlado por while
primeiro_termo, razao = 2, 3
termo = primeiro_termo
contador = 0
while contador < 10:
    print(termo, end=" ")
    termo += razao
    contador += 1


# --- Exercicio 62 - Super Progressao Aritmetica -----------------------------
# Tema: PA com opcao de mostrar mais termos (loop de continuacao)
termo = 2
razao = 3
mostrar_mais = True
qtd_mostrados = 0
while mostrar_mais:
    print(termo, end=" ")
    termo += razao
    qtd_mostrados += 1
    if qtd_mostrados == 10:
        mostrar_mais = False   # em codigo real, perguntaria ao usuario aqui


# --- Exercicio 63 - Sequencia de Fibonacci --------------------------------
# Tema: dois acumuladores trocando de valor a cada iteracao
a, b = 0, 1
qtd_termos = 10
contador = 0
while contador < qtd_termos:
    print(a, end=" ")
    a, b = b, a + b     # troca simultanea: a vira b, b vira a soma anterior
    contador += 1


# --- Exercicio 64 - Tratando varios valores ---------------------------------
# Tema: while com contador de itens processados
valores = [3, 8, -1, 5, -1]   # -1 marca o fim da entrada
i = 0
soma = 0
while valores[i] != -1:
    soma += valores[i]
    i += 1
print(f"Soma total: {soma}")


# --- Exercicio 65 - Maior e Menor valores -------------------------------------
# Tema: mesmo padrao do ex. 55, controlado por while + flag de parada
valores = [4, 9, 1, 7]
i = 0
maior = menor_valor = valores[0]
while i < len(valores):
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor_valor:
        menor_valor = valores[i]
    i += 1
print(f"Maior: {maior} | Menor: {menor_valor}")


# --- Exercicio 66 - Varios numeros com flag ------------------------------------
# Tema: uso explicito de variavel flag (continuar = 'S')
continuar = 'S'
contagem = 0
while continuar == 'S':
    contagem += 1
    # em codigo real: continuar = input("Continuar? (S/N) ").upper()
    continuar = 'N' if contagem >= 3 else 'S'   # simulacao
print(f"Total de rodadas: {contagem}")


# --- Exercicio 67 - Tabuada v3.0 --------------------------------------------
# Tema: tabuada controlada por while, com opcao de repetir
numero = 5
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1


# --- Exercicio 68 - Jogo do Par ou Impar ---------------------------------------
# Tema: while + random, logica de vitoria/derrota
import random
computador = random.randint(0, 10)
jogador = 4
escolha = "PAR"
soma = computador + jogador
resultado_par = (soma % 2 == 0)
if (escolha == "PAR" and resultado_par) or (escolha == "IMPAR" and not resultado_par):
    print("Jogador venceu")
else:
    print("Computador venceu")


# --- Exercicio 69 - Analise de dados do grupo -----------------------------------
# Tema: acumuladores multiplos (contagem, soma, media) dentro de um while
idades = [22, 35, 19, 41]
i = 0
soma_idades = 0
while i < len(idades):
    soma_idades += idades[i]
    i += 1
media = soma_idades / len(idades)
print(f"Media de idade do grupo: {media:.1f}")


# --- Exercicio 70 - Estatisticas em produtos --------------------------------------
# Tema: acumuladores com condicoes (maior valor, quantos acima da media)
precos = [50, 120, 30, 200, 80]
i = 0
soma = 0
while i < len(precos):
    soma += precos[i]
    i += 1
media = soma / len(precos)
acima_da_media = 0
for p in precos:            # segunda passada, agora com for
    if p > media:
        acima_da_media += 1
print(f"Media: {media:.2f} | Produtos acima da media: {acima_da_media}")


# --- Exercicio 71 - Simulador de Caixa Eletronico -----------------------------------
# Tema: divisao sucessiva por cedulas usando while
valor_saque = 356
cedulas = [100, 50, 20, 10, 5, 2, 1]
restante = valor_saque
for cedula in cedulas:
    qtd = restante // cedula        # quantas cedulas desse valor cabem
    if qtd > 0:
        print(f"{qtd} nota(s) de R$ {cedula}")
        restante -= qtd * cedula    # while implicito: continua ate restante = 0

# ATENCAO neste bloco:
# - garantir que a condicao do while mude a cada iteracao (senao trava)
# - cuidado com input() sem validacao dentro do loop (tema do ex. 57)


# =============================================================
# ERROS MAIS COMUNS NO MUNDO 2 (GERAL)
# =============================================================
# 1. Esquecer de converter input() para int/float antes de comparar/calcular
#    ex: idade = input("Idade: ")       -> ERRADO (idade vira string)
#        idade = int(input("Idade: "))  -> CERTO
#
# 2. Confundir '=' (atribuicao) com '==' (comparacao)
#    ex: if x = 5:   -> SyntaxError
#        if x == 5:  -> correto
#
# 3. Loop infinito por esquecer de atualizar a variavel de controle no while
#    ex: while x < 10:
#            print(x)          # falta "x += 1" -> nunca termina
#
# 4. Off-by-one em range() -> range(1, 10) vai ate 9, nao ate 10
#
# 5. Indentacao inconsistente misturando espacos e tabs