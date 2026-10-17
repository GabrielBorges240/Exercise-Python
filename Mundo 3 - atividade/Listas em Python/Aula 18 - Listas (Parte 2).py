# =====================================================================
# AULA 18 - LISTAS (PARTE 2)  |  Curso em Vídeo - Python 3 - Mundo 3
# Dica: rode um bloco de cada vez. Para isso, comente (Ctrl + ;) os
# outros blocos ou use "Run Selection/Line in Terminal" (Shift+Enter).
# =====================================================================


# ---------------------------------------------------------------------
# PARTE 1 - O QUE É UMA LISTA?
# ---------------------------------------------------------------------
# Lista = variável composta: guarda VÁRIOS valores em UMA variável.
# Cada valor tem uma posição (índice), começando em 0.
# Listas são MUTÁVEIS (diferente de tuplas): dá para alterar depois.

print('--- 1. Criando e acessando ---')
lanche = ['hambúrguer', 'suco', 'pizza', 'pudim']
#            índice 0      1       2        3
print(lanche)          # mostra a lista inteira
print(lanche[0])       # primeiro item  -> hambúrguer
print(lanche[-1])      # último item    -> pudim (índice negativo conta do fim)
print(lanche[1:3])     # fatiamento: do 1 até ANTES do 3 -> ['suco', 'pizza']

# Mudando um valor (só funciona porque lista é mutável)
lanche[3] = 'picolé'
print(lanche)


# ---------------------------------------------------------------------
# PARTE 2 - ADICIONANDO ITENS: append e insert
# ---------------------------------------------------------------------
print('\n--- 2. append e insert ---')
lanche.append('cookie')      # adiciona NO FINAL
print(lanche)
lanche.insert(0, 'cachorro-quente')  # insert(posição, valor): coloca na posição
print(lanche)


# ---------------------------------------------------------------------
# PARTE 3 - REMOVENDO ITENS: del, pop e remove
# ---------------------------------------------------------------------
print('\n--- 3. del, pop e remove ---')
lanche = ['hambúrguer', 'suco', 'pizza', 'pudim', 'pizza']

del lanche[3]            # apaga pelo ÍNDICE (não devolve nada)
print(lanche)

lanche.pop(3)            # apaga pelo índice; sem número apaga o ÚLTIMO
print(lanche)

lanche.remove('pizza')   # apaga pelo VALOR (só a PRIMEIRA ocorrência)
print(lanche)

# Cuidado: remove() de um valor que não existe dá ERRO (ValueError).
# Por isso é comum testar antes:
if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)


# ---------------------------------------------------------------------
# PARTE 4 - CRIANDO LISTAS COM range()
# ---------------------------------------------------------------------
print('\n--- 4. list(range()) ---')
valores = list(range(4, 11))     # 4,5,6,...,10 (o 11 NÃO entra)
print(valores)
pares = list(range(0, 21, 2))    # de 0 a 20, de 2 em 2
print(pares)


# ---------------------------------------------------------------------
# PARTE 5 - ORGANIZANDO: sort, reverse, len
# ---------------------------------------------------------------------
print('\n--- 5. sort, reverse e len ---')
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()                   # ordena crescente (MUDA a lista original)
print(valores)
valores.sort(reverse=True)       # ordena decrescente
print(valores)
print(f'A lista tem {len(valores)} elementos.')   # len = quantidade de itens
print(f'Maior: {max(valores)} | Menor: {min(valores)} | Soma: {sum(valores)}')


# ---------------------------------------------------------------------
# PARTE 6 - PEGADINHA CLÁSSICA: COPIAR LISTAS
# ---------------------------------------------------------------------
# Esse é o ponto que mais derruba iniciante. Atenção!
print('\n--- 6. Copiando listas ---')

a = [2, 3, 4, 7]
b = a                # NÃO copia! Cria um "apelido": a e b são a MESMA lista
b[2] = 8
print(f'a = {a}')    # a também mudou!
print(f'b = {b}')

a = [2, 3, 4, 7]
b = a[:]             # copia de verdade (fatiamento completo)
b[2] = 8
print(f'a = {a}')    # a continua igual
print(f'b = {b}')    # só b mudou
# Outra forma de copiar: b = a.copy()


# ---------------------------------------------------------------------
# PARTE 7 - PERCORRENDO LISTAS COM for
# ---------------------------------------------------------------------
print('\n--- 7. Percorrendo com for ---')
frutas = ['maçã', 'banana', 'uva']

for fruta in frutas:                    # pega cada VALOR
    print(f'Eu gosto de {fruta}')

for posicao, fruta in enumerate(frutas):  # pega POSIÇÃO e VALOR juntos
    print(f'Na posição {posicao} está {fruta}')


# ---------------------------------------------------------------------
# PARTE 8 - LER VALORES DO USUÁRIO E GUARDAR NA LISTA
# ---------------------------------------------------------------------
print('\n--- 8. Lendo valores ---')
numeros = []                      # lista vazia para começar
while True:
    n = int(input('Digite um número (0 para parar): '))
    if n == 0:
        break
    numeros.append(n)             # guarda cada número digitado
print(f'Você digitou: {numeros}')


# =====================================================================
# ATIVIDADES (resolva você mesmo antes de olhar a solução!)
# Dica para seu jeito de estudar: escreva primeiro o passo a passo em
# pseudocódigo (em comentário) e só depois o código.
# =====================================================================

# ---------------------------------------------------------------------
# ATIVIDADE 1 - Lista de compras
# Enunciado: crie uma lista vazia. Peça 3 itens ao usuário e adicione
# cada um com append. No final, mostre a lista e a quantidade de itens.
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. criar lista vazia
#   2. repetir 3 vezes: ler item -> append na lista
#   3. mostrar lista e len(lista)

compras = []
for c in range(3):
    item = input(f'Item {c + 1}: ')
    compras.append(item)
print(f'Lista: {compras}')
print(f'Total de itens: {len(compras)}')


# ---------------------------------------------------------------------
# ATIVIDADE 2 - Maior e menor, com posição
# Enunciado: leia 5 números, guarde em lista e mostre:
#   a) a lista ordenada  b) o maior e em que posição estava
#   c) o menor e em que posição estava (na lista ORIGINAL)
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. ler 5 números e guardar
#   2. maior = max(lista), menor = min(lista)
#   3. posição = lista.index(valor)  -> index() devolve o índice do valor
#   4. ordenar uma CÓPIA (para não perder a ordem original)

numeros = []
for c in range(5):
    numeros.append(int(input(f'Número {c + 1}: ')))

maior = max(numeros)
menor = min(numeros)
print(f'Ordem original: {numeros}')
print(f'Maior: {maior} na posição {numeros.index(maior)}')
print(f'Menor: {menor} na posição {numeros.index(menor)}')

ordenada = numeros[:]   # cópia! (lembra da Parte 6?)
ordenada.sort()
print(f'Ordenada: {ordenada}')


# ---------------------------------------------------------------------
# ATIVIDADE 3 - Separando pares e ímpares
# Enunciado: leia 6 números. Crie duas listas (pares e ímpares) e mostre
# cada uma ordenada.
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. criar listas pares e impares vazias
#   2. para cada número lido: se n % 2 == 0 -> pares, senão -> impares
#   3. ordenar e mostrar

pares = []
impares = []
for c in range(6):
    n = int(input(f'Número {c + 1}: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')


# ---------------------------------------------------------------------
# ATIVIDADE 4 - Sem repetidos
# Enunciado: leia números até o usuário digitar 0. Só adicione na lista
# se o número ainda NÃO estiver nela. Se repetido, avise.
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. loop infinito; ler n
#   2. se n == 0 -> break
#   3. se n in lista -> avisar; senão -> append

lista = []
while True:
    n = int(input('Digite um número (0 para sair): '))
    if n == 0:
        break
    if n in lista:
        print('Valor duplicado! Não vou adicionar.')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
print(f'Valores únicos em ordem: {sorted(lista)}')   # sorted() não altera a original


# ---------------------------------------------------------------------
# ATIVIDADE 5 (DESAFIO) - Inverter sem usar reverse()
# Enunciado: dada a lista [1, 2, 3, 4, 5], crie uma nova lista com os
# valores em ordem inversa usando for + insert(0, valor).
# Depois confira com lista[::-1].
# ---------------------------------------------------------------------
original = [1, 2, 3, 4, 5]
invertida = []
for valor in original:
    invertida.insert(0, valor)    # sempre coloca no começo
print(f'Invertida (insert): {invertida}')
print(f'Invertida (fatia):  {original[::-1]}')


# =====================================================================
# RESUMO RÁPIDO (cola para revisar)
# lista.append(x)       adiciona no final
# lista.insert(i, x)    adiciona na posição i
# del lista[i]          remove pelo índice
# lista.pop(i)          remove pelo índice (sem i = último)
# lista.remove(x)       remove pelo valor (1ª ocorrência)
# list(range(a, b, p))  cria lista de números
# lista.sort()          ordena (altera a lista)
# sorted(lista)         ordena e devolve uma nova lista
# len(lista)            quantidade de itens
# lista.index(x)        posição do valor x
# b = a[:]              copia de verdade (b = a só cria apelido)
# =====================================================================