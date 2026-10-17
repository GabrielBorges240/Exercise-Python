# ==============================================================================
# AULA 17 - LISTAS EM PYTHON (PARTE 1)
# Curso em Vídeo - Python 3 - Mundo 3
# ==============================================================================
#
# O QUE SÃO LISTAS?
# Listas são variáveis compostas (heterogêneas) que armazenam vários valores
# em uma única estrutura. Cada valor é acessado por um índice (posição),
# que começa em 0 (zero).
#
# Diferente de outras linguagens, em Python uma lista pode guardar tipos
# diferentes de dados ao mesmo tempo (int, str, float, bool, outra lista...).
# ==============================================================================


# ------------------------------------------------------------------------
# 1. CRIANDO UMA LISTA
# ------------------------------------------------------------------------
# Usamos colchetes [ ] e separamos os valores por vírgula.

lista_vazia = []
frutas = ['maçã', 'banana', 'uva', 'pera']
numeros = [10, 20, 30, 40, 50]
mista = ['Gustavo', 45, 1.83, True]  # tipos diferentes na mesma lista

print(frutas)   # ['maçã', 'banana', 'uva', 'pera']
print(numeros)  # [10, 20, 30, 40, 50]
print(mista)    # ['Gustavo', 45, 1.83, True]


# ------------------------------------------------------------------------
# 2. ACESSANDO ELEMENTOS (ÍNDICES)
# ------------------------------------------------------------------------
# O primeiro elemento é o índice 0, o segundo é o índice 1, e assim por diante.

print(frutas[0])  # maçã
print(frutas[2])  # uva

# Índices NEGATIVOS acessam a lista de trás para frente.
# -1 é o último elemento, -2 é o penúltimo...

print(frutas[-1])  # pera  (último)
print(frutas[-2])  # uva   (penúltimo)


# ------------------------------------------------------------------------
# 3. FATIAMENTO (SLICING)
# ------------------------------------------------------------------------
# Podemos pegar uma "fatia" da lista usando lista[inicio:fim]
# OBS: o elemento do índice "fim" NÃO entra no resultado.

print(numeros[1:3])   # [20, 30]  -> pega índices 1 e 2
print(numeros[:2])    # [10, 20]  -> do começo até o índice 1
print(numeros[2:])    # [30, 40, 50] -> do índice 2 até o final
print(numeros[:])     # [10, 20, 30, 40, 50] -> copia a lista inteira


# ------------------------------------------------------------------------
# 4. MODIFICANDO ELEMENTOS
# ------------------------------------------------------------------------
# Diferente de strings, LISTAS SÃO MUTÁVEIS: podemos alterar um valor
# diretamente pelo índice.

frutas[0] = 'melancia'
print(frutas)  # ['melancia', 'banana', 'uva', 'pera']


# ------------------------------------------------------------------------
# 5. PRINCIPAIS MÉTODOS DE LISTA
# ------------------------------------------------------------------------

nomes = ['Ana', 'Bruno', 'Carlos']

# append() -> adiciona um item no FINAL da lista
nomes.append('Diana')
print(nomes)  # ['Ana', 'Bruno', 'Carlos', 'Diana']

# insert(posicao, valor) -> insere um item em uma posição específica
nomes.insert(1, 'Eduardo')
print(nomes)  # ['Ana', 'Eduardo', 'Bruno', 'Carlos', 'Diana']

# remove(valor) -> remove a PRIMEIRA ocorrência do valor
nomes.remove('Carlos')
print(nomes)  # ['Ana', 'Eduardo', 'Bruno', 'Diana']

# pop() -> remove e RETORNA o último item (ou o item de um índice, se informado)
ultimo = nomes.pop()
print(ultimo)  # Diana
print(nomes)   # ['Ana', 'Eduardo', 'Bruno']

removido = nomes.pop(0)  # remove pelo índice
print(removido)  # Ana
print(nomes)      # ['Eduardo', 'Bruno']

# len() -> quantidade de elementos na lista
print(len(nomes))  # 2

# sort() -> ordena a lista (por padrão, ordem crescente)
numeros_bagunçados = [5, 2, 9, 1, 7]
numeros_bagunçados.sort()
print(numeros_bagunçados)  # [1, 2, 5, 7, 9]

numeros_bagunçados.sort(reverse=True)  # ordem decrescente
print(numeros_bagunçados)  # [9, 7, 5, 2, 1]

# reverse() -> inverte a ordem atual da lista (não ordena, só inverte)
letras = ['a', 'b', 'c', 'd']
letras.reverse()
print(letras)  # ['d', 'c', 'b', 'a']

# count(valor) -> conta quantas vezes um valor aparece
repetidos = [1, 2, 2, 3, 2, 4]
print(repetidos.count(2))  # 3

# in -> verifica se um valor EXISTE na lista (retorna True/False)
print('Bruno' in nomes)     # True
print('Carlos' in nomes)    # False


# ------------------------------------------------------------------------
# 6. PERCORRENDO UMA LISTA COM FOR
# ------------------------------------------------------------------------

cores = ['azul', 'verde', 'amarelo']

for cor in cores:
    print(cor)
# azul
# verde
# amarelo

# Se precisar do ÍNDICE junto com o valor, usamos enumerate()
for indice, cor in enumerate(cores):
    print(f'{indice} -> {cor}')
# 0 -> azul
# 1 -> verde
# 2 -> amarelo


# ------------------------------------------------------------------------
# 7. LISTAS ANINHADAS (lista dentro de lista)
# ------------------------------------------------------------------------

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0])     # [1, 2, 3]  -> primeira "linha"
print(matriz[0][1])  # 2          -> elemento da linha 0, coluna 1
print(matriz[2][2])  # 9          -> elemento da linha 2, coluna 2


# ==============================================================================
# EXERCÍCIOS RESOLVIDOS
# ==============================================================================

# ------------------------------------------------------------------------
# EXERCÍCIO 1
# Crie uma lista com 5 números e mostre a soma e a média deles.
# ------------------------------------------------------------------------

valores = [4, 8, 15, 16, 23]
soma = sum(valores)          # sum() soma todos os elementos da lista
media = soma / len(valores)  # len() dá a quantidade de elementos

print(f'Soma: {soma}')     # Soma: 66
print(f'Média: {media}')   # Média: 13.2

# EXPLICAÇÃO:
# - sum(lista) é uma função pronta do Python que soma os valores.
# - len(lista) retorna quantos elementos existem, usado para calcular a média.


# ------------------------------------------------------------------------
# EXERCÍCIO 2
# Peça 5 nomes ao usuário, guarde numa lista e depois mostre em ordem
# alfabética.
# ------------------------------------------------------------------------

pessoas = []
for i in range(5):
    nome = input(f'Digite o {i+1}º nome: ')
    pessoas.append(nome)

pessoas.sort()
print('Lista em ordem alfabética:')
print(pessoas)

# EXPLICAÇÃO:
# - range(5) gera 5 repetições (0,1,2,3,4).
# - A cada volta do for, pedimos um nome com input() e usamos append()
#   para adicionar esse nome ao final da lista "pessoas".
# - sort() organiza a lista em ordem alfabética (ordem crescente para strings).


# ------------------------------------------------------------------------
# EXERCÍCIO 3
# Dada uma lista de números, separe os PARES e os ÍMPARES em duas
# listas diferentes.
# ------------------------------------------------------------------------

numeros_ex3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for n in numeros_ex3:
    if n % 2 == 0:       # resto da divisão por 2 igual a 0 => número par
        pares.append(n)
    else:
        impares.append(n)

print(f'Pares: {pares}')      # Pares: [2, 4, 6, 8, 10]
print(f'Ímpares: {impares}')  # Ímpares: [1, 3, 5, 7, 9]

# EXPLICAÇÃO:
# - O operador % (módulo) retorna o resto de uma divisão.
# - Se n % 2 == 0, o número é divisível por 2 exatamente, ou seja, é par.
# - Usamos append() para ir guardando cada número na lista correta.


# ------------------------------------------------------------------------
# EXERCÍCIO 4
# Crie um programa que mostra o maior e o menor valor de uma lista,
# SEM usar as funções prontas max() e min() (para treinar lógica).
# ------------------------------------------------------------------------

numeros_ex4 = [34, 12, 87, 5, 63, 29]

maior = numeros_ex4[0]  # começamos assumindo que o primeiro é o maior
menor = numeros_ex4[0]  # e também o menor

for n in numeros_ex4:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'Maior valor: {maior}')  # Maior valor: 87
print(f'Menor valor: {menor}')  # Menor valor: 5

# EXPLICAÇÃO:
# - Guardamos o primeiro elemento como referência inicial de maior e menor.
# - Percorremos a lista comparando cada número:
#   se for maior que o "maior" atual, atualizamos; o mesmo para o menor.
# - No fim do laço, "maior" e "menor" terão os valores corretos.
# - (Na prática, o Python já tem max(lista) e min(lista) prontos para isso.)


# ------------------------------------------------------------------------
# EXERCÍCIO 5
# Some 5 valores digitados pelo usuário, mas mostre também
# de quais posições vieram os 3 maiores valores.
# ------------------------------------------------------------------------

valores_digitados = []
for i in range(5):
    v = int(input(f'Digite o {i+1}º valor: '))
    valores_digitados.append(v)

# sorted() cria uma NOVA lista ordenada, sem alterar a original
maiores = sorted(valores_digitados, reverse=True)[:3]

print(f'Valores digitados: {valores_digitados}')
print(f'Os 3 maiores valores foram: {maiores}')

# EXPLICAÇÃO:
# - sorted(lista, reverse=True) devolve uma lista nova ordenada do
#   maior para o menor, sem modificar "valores_digitados".
# - [:3] pega os 3 primeiros elementos dessa lista já ordenada,
#   ou seja, os 3 maiores valores digitados.


# ==============================================================================
# DICA IMPORTANTE: LISTA É MUTÁVEL (CUIDADO AO "COPIAR")
# ==============================================================================
a = [1, 2, 3]
b = a          # isso NÃO cria uma cópia, "b" aponta para a MESMA lista
b.append(4)
print(a)       # [1, 2, 3, 4]  -> "a" também mudou!

# Para copiar de verdade, use:
c = a.copy()   # ou c = a[:]  ou  c = list(a)
c.append(99)
print(a)       # [1, 2, 3, 4]      -> não mudou
print(c)       # [1, 2, 3, 4, 99]  -> só a cópia mudou