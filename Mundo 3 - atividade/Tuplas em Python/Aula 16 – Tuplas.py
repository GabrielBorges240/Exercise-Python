# ============================================================
# AULA 16 - TUPLAS | Python 3 - Mundo 3 | Curso em Vídeo
# ============================================================
#
# O QUE É UMA TUPLA?
#   - É uma VARIÁVEL COMPOSTA: guarda vários valores em uma só variável.
#   - É IMUTÁVEL: depois de criada, não dá para trocar, adicionar
#     nem remover itens.
#   - Cada item tem uma posição (índice), começando em 0.
#   - Escreve-se com parênteses: ( )
#
# QUANDO USAR?
#   Para dados que não devem mudar: dias da semana, meses, coordenadas,
#   uma ficha fixa (nome, idade, altura) etc.
#
# ÍNDICES (exemplo com 5 itens):
#   posição:   0    1    2    3    4
#   negativo: -5   -4   -3   -2   -1
#
# RESUMO DO QUE A TUPLA TEM:
#   len(t)        quantidade de itens
#   t[i]          item na posição i
#   t[a:b]        fatia (do índice a até b-1)
#   t.count(x)    quantas vezes x aparece
#   t.index(x)    posição da primeira ocorrência de x
#   sorted(t)     itens ordenados (devolve uma LISTA)
#   t1 + t2       junta duas tuplas (cria uma nova)
#   x in t        verifica se x está na tupla (True/False)
#   max, min, sum maior, menor e soma dos itens
#
# Dica: antes de rodar cada linha, tente prever o resultado.


# ------------------------------------------------------------
# PARTE 1 - CRIANDO TUPLAS
# ------------------------------------------------------------
print("=== PARTE 1: CRIANDO TUPLAS ===")

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche)               # ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(type(lanche))         # <class 'tuple'>
print(len(lanche))          # 5

# Tupla com UM item só: precisa da vírgula!
uma = (5,)
nao_e_tupla = (5)
print(type(uma))            # <class 'tuple'>
print(type(nao_e_tupla))    # <class 'int'>  (é só o número 5 entre parênteses)

# Os parênteses são opcionais na criação
sem_parenteses = 1, 2, 3
print(sem_parenteses)       # (1, 2, 3)


# ------------------------------------------------------------
# PARTE 2 - ACESSANDO ITENS E FATIANDO
# ------------------------------------------------------------
print("\n=== PARTE 2: ÍNDICES E FATIAS ===")

print(lanche[0])            # hambúrguer  (primeiro)
print(lanche[1])            # suco
print(lanche[-1])           # batata frita (último)
print(lanche[-2])           # pudim (penúltimo)

# Fatiamento [início:fim] -> o fim NÃO é incluído
print(lanche[1:3])          # ('suco', 'pizza')
print(lanche[2:])           # ('pizza', 'pudim', 'batata frita')
print(lanche[:2])           # ('hambúrguer', 'suco')
print(lanche[-2:])          # ('pudim', 'batata frita')
print(lanche[::2])          # ('hambúrguer', 'pizza', 'batata frita')  (de 2 em 2)
print(lanche[::-1])         # ('batata frita', 'pudim', 'pizza', 'suco', 'hambúrguer')  (invertida)


# ------------------------------------------------------------
# PARTE 3 - PERCORRENDO COM for
# ------------------------------------------------------------
print("\n=== PARTE 3: PERCORRENDO A TUPLA ===")

# 1) direto nos itens
for comida in lanche:
    print(f'Eu vou comer {comida}')

# 2) pelas posições com range(len())
for pos in range(len(lanche)):
    print(f'{pos} -> {lanche[pos]}')

# 3) posição e item ao mesmo tempo com enumerate
for pos, comida in enumerate(lanche):
    print(f'Na posição {pos} tem {comida}')


# ------------------------------------------------------------
# PARTE 4 - JUNTANDO E CONSULTANDO
# ------------------------------------------------------------
print("\n=== PARTE 4: OPERAÇÕES E MÉTODOS ===")

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)                    # (2, 5, 4, 5, 8, 1, 2)
print(len(c))               # 7
print(c.count(5))           # 2   (o 5 aparece duas vezes)
print(c.count(9))           # 0
print(c.index(8))           # 4   (posição do 8)
print(c.index(5))           # 1   (primeira ocorrência do 5)
print(c.index(5, 2))        # 3   (procura o 5 a partir da posição 2)
print(max(c))               # 8
print(min(c))               # 1
print(sum(c))               # 27
print(8 in c)               # True
print(9 in c)               # False
print(a * 2)                # (2, 5, 4, 2, 5, 4)

# sorted() devolve uma LISTA. Para voltar a ser tupla, use tuple()
print(sorted(c))            # [1, 2, 2, 4, 5, 5, 8]
print(tuple(sorted(c)))     # (1, 2, 2, 4, 5, 5, 8)


# ------------------------------------------------------------
# PARTE 5 - TUPLAS SÃO IMUTÁVEIS
# ------------------------------------------------------------
print("\n=== PARTE 5: IMUTABILIDADE ===")

# Tentar trocar um item dá ERRO (por isso está comentado):
# lanche[1] = 'refrigerante'   # TypeError: 'tuple' object does not support item assignment

# Para "alterar", crie uma NOVA tupla juntando pedaços:
novo_lanche = lanche[:1] + ('refrigerante',) + lanche[2:]
print(novo_lanche)          # ('hambúrguer', 'refrigerante', 'pizza', 'pudim', 'batata frita')
print(lanche)               # a original continua igual

# Não dá para apagar UM item, só a tupla INTEIRA:
temporaria = (1, 2, 3)
del temporaria
# print(temporaria)         # NameError: name 'temporaria' is not defined


# ------------------------------------------------------------
# PARTE 6 - EXERCÍCIOS RESOLVIDOS
# (troque os valores fixos por input() se quiser testar outros)
# ------------------------------------------------------------
print("\n=== PARTE 6: EXERCÍCIOS ===")

# Ex 1 - Mostrar a primeira fruta, a última e as três primeiras
frutas = ('maçã', 'banana', 'uva', 'manga', 'pera')
print('Ex 1 primeira:', frutas[0])        # maçã
print('Ex 1 última:', frutas[-1])         # pera
print('Ex 1 três primeiras:', frutas[:3]) # ('maçã', 'banana', 'uva')

# Ex 2 - Listar as frutas numeradas (enumerate)
for pos, fruta in enumerate(frutas):
    print(f'Ex 2: {pos + 1}º {fruta}')    # 1º maçã, 2º banana, ... 5º pera

# Ex 3 - Quantidade, maior, menor, soma e média de uma tupla de números
numeros = (7, 12, 3, 20, 15, 8)
quantidade = len(numeros)                 # 6
soma = sum(numeros)                       # 65
media = soma / quantidade                 # 10.833...
print(f'Ex 3: {quantidade} números | maior = {max(numeros)} | menor = {min(numeros)}')
print(f'Ex 3: soma = {soma} | média = {media:.2f}')   # soma = 65 | média = 10.83

# Ex 4 - Separar pares e ímpares (usa % e if/else)
pares = ()
impares = ()
for n in numeros:
    if n % 2 == 0:
        pares += (n,)     # cria uma nova tupla e guarda na mesma variável
    else:
        impares += (n,)
print('Ex 4: pares =', pares)             # (12, 20, 8)
print('Ex 4: ímpares =', impares)         # (7, 3, 15)

# Ex 5 - Nomes em ordem alfabética e em ordem inversa
nomes = ('Carlos', 'Ana', 'Marcos', 'Beatriz', 'Julia')
print('Ex 5:', tuple(sorted(nomes)))                # ('Ana', 'Beatriz', 'Carlos', 'Julia', 'Marcos')
print('Ex 5:', tuple(sorted(nomes, reverse=True)))  # ('Marcos', 'Julia', 'Carlos', 'Beatriz', 'Ana')

# Ex 6 - Procurar um valor: quantas vezes, em que posições, e se existe
valores = (4, 9, 2, 9, 7, 9)
print('Ex 6: o 9 aparece', valores.count(9), 'vezes')      # 3 vezes
for pos, v in enumerate(valores):
    if v == 9:
        print(f'Ex 6: o 9 está na posição {pos}')          # 1, 3 e 5
if 5 in valores:
    print('Ex 6: o 5 está na tupla')
else:
    print('Ex 6: o 5 NÃO está na tupla')                   # este é o resultado

# Ex 7 - Ficha de uma pessoa (nome, idade, altura) com condição
pessoa = ('Ana', 21, 1.65)
print(f'Ex 7: Nome: {pessoa[0]} | Idade: {pessoa[1]} | Altura: {pessoa[2]} m')
nome, idade, altura = pessoa              # desempacotamento: cada valor vai para uma variável
if idade >= 18:
    print(f'Ex 7: {nome} é maior de idade')                # este é o resultado
else:
    print(f'Ex 7: {nome} é menor de idade')

# Ex 8 - Classificação: primeiros, últimos, ordem alfabética e posição
classificacao = ('Azul', 'Verde', 'Amarelo', 'Roxo', 'Preto', 'Branco', 'Laranja', 'Rosa')
print('Ex 8: 3 primeiros =', classificacao[:3])      # ('Azul', 'Verde', 'Amarelo')
print('Ex 8: 2 últimos =', classificacao[-2:])       # ('Laranja', 'Rosa')
print('Ex 8: alfabética =', tuple(sorted(classificacao)))
# ('Amarelo', 'Azul', 'Branco', 'Laranja', 'Preto', 'Rosa', 'Roxo', 'Verde')
print('Ex 8: Roxo está na posição', classificacao.index('Roxo') + 1)   # 4 (índice 3 + 1)

# Ex 9 - Juntar e repetir tuplas
t1 = (1, 2, 3)
t2 = (3, 4)
junto = t1 + t2
print('Ex 9:', junto)                     # (1, 2, 3, 3, 4)
print('Ex 9:', t1 * 2)                    # (1, 2, 3, 1, 2, 3)
print('Ex 9: o 3 aparece', junto.count(3), 'vezes')   # 2 vezes

# Ex 10 - Converter segundos em minutos e segundos (usa // e %)
tempos = (135, 60, 200)
for t in tempos:
    print(f'Ex 10: {t} s = {t // 60} min e {t % 60} s')
# 135 s = 2 min e 15 s | 60 s = 1 min e 0 s | 200 s = 3 min e 20 s

# Ex 11 - Média de notas com if/elif/else
notas = (6.5, 8.0, 5.0, 9.5)
media_notas = sum(notas) / len(notas)     # 29.0 / 4 = 7.25
if media_notas >= 7:
    situacao = 'aprovado'
elif media_notas >= 5:
    situacao = 'recuperação'
else:
    situacao = 'reprovado'
print(f'Ex 11: média {media_notas:.2f} -> {situacao}')   # média 7.25 -> aprovado


# ------------------------------------------------------------
# PARTE 7 - DESAFIOS PARA FAZER SOZINHO (sem resposta)
# Escreva o código abaixo de cada desafio e compare com o esperado.
# ------------------------------------------------------------

# Desafio 1: dada a tupla (3, 8, 5, 10, 6), mostre só os números
#            MAIORES que 5.
#            Esperado: 8, 10 e 6

# Desafio 2: dada a tupla (9, 4, 12, 7, 15, 10), mostre quantos números
#            são múltiplos de 3 (dica: use %).
#            Esperado: 3

# Desafio 3: dada a tupla ('a', 'b', 'c', 'd', 'e'), mostre-a em ordem
#            inversa usando fatiamento.
#            Esperado: ('e', 'd', 'c', 'b', 'a')