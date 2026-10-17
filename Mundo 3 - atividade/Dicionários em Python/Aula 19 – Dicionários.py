# =====================================================================
# AULA 19 - DICIONÁRIOS  |  Curso em Vídeo - Python 3 - Mundo 3
# Dica: rode um bloco de cada vez (selecione e use Shift+Enter) ou
# comente os blocos que não quer executar (Ctrl + ;).
# =====================================================================


# ---------------------------------------------------------------------
# PARTE 1 - O QUE É UM DICIONÁRIO?
# ---------------------------------------------------------------------
# Lista  -> acessa por POSIÇÃO (índice): lista[0]
# Dicionário -> acessa por CHAVE (nome):   dados['nome']
# Estrutura: { chave: valor, chave: valor, ... }
# Dicionários usam CHAVES { }, listas usam COLCHETES [ ].

print('--- 1. Criando e acessando ---')
dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
print(dados['nome'])      # acessa pela chave -> Pedro
print(dados['idade'])     # -> 25
# dados[0] daria ERRO (KeyError): não existe chave 0 aqui.

# Dicionário vazio (duas formas):
vazio = {}
vazio2 = dict()


# ---------------------------------------------------------------------
# PARTE 2 - ADICIONAR, ALTERAR E APAGAR
# ---------------------------------------------------------------------
print('\n--- 2. Adicionar, alterar e apagar ---')
dados['sexo'] = 'M'       # chave NOVA -> adiciona (não existe append!)
print(dados)

dados['nome'] = 'Maria'   # chave que JÁ existe -> altera o valor
print(dados)

del dados['idade']        # apaga a chave (e o valor junto)
print(dados)


# ---------------------------------------------------------------------
# PARTE 3 - values(), keys() e items()
# ---------------------------------------------------------------------
print('\n--- 3. values, keys, items ---')
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

print(filme.values())   # só os VALORES
print(filme.keys())     # só as CHAVES
print(filme.items())    # pares (chave, valor)

# Para o programa não "quebrar" ao buscar uma chave que talvez não exista:
print(filme.get('nota'))            # None (sem erro)
print(filme.get('nota', 'sem nota'))  # valor padrão se não existir
print('ano' in filme)               # True: 'in' testa CHAVES


# ---------------------------------------------------------------------
# PARTE 4 - PERCORRENDO COM for
# ---------------------------------------------------------------------
print('\n--- 4. Percorrendo com for ---')

for k in filme.keys():                # só as chaves (é o padrão se omitir .keys())
    print(f'Chave: {k}')

for v in filme.values():              # só os valores
    print(f'Valor: {v}')

for k, v in filme.items():            # chave E valor juntos (o mais usado)
    print(f'O {k} é {v}')


# ---------------------------------------------------------------------
# PARTE 5 - DICIONÁRIO DENTRO DE LISTA (muito usado!)
# ---------------------------------------------------------------------
# Uma lista guarda VÁRIOS dicionários: cada dicionário é um "registro"
# (como uma linha de tabela). Isso é a base de dados vindos de APIs/JSON.
print('\n--- 5. Lista de dicionários ---')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])   # [1] escolhe o dicionário, ['sigla'] escolhe a chave

for e in brasil:
    print(f"{e['uf']} -> {e['sigla']}")   # aspas diferentes dentro da f-string!


# ---------------------------------------------------------------------
# PARTE 6 - PEGADINHA CLÁSSICA: COPIAR DICIONÁRIO
# ---------------------------------------------------------------------
# Igual às listas: "b = a" NÃO copia, só cria apelido.
print('\n--- 6. Copiando ---')
a = {'x': 1}
b = a
b['x'] = 99
print(a)          # a mudou junto!

a = {'x': 1}
b = a.copy()      # copia de verdade
b['x'] = 99
print(a, b)       # a intacto

# E o erro mais comum com listas de dicionários:
# se você faz append(estado) e depois só muda o MESMO dicionário,
# todos os itens da lista ficam iguais. Solução: append(estado.copy()).
print('\n--- 6b. Erro clássico ---')
estado = {}
lista = []
for uf in ['RJ', 'SP', 'MG']:
    estado['sigla'] = uf
    lista.append(estado.copy())   # sem .copy(), a lista teria 3x 'MG'
print(lista)


# =====================================================================
# ATIVIDADES (tente sozinho antes de olhar a solução!)
# Faça primeiro o pseudocódigo em comentário, depois o código.
# =====================================================================

# ---------------------------------------------------------------------
# ATIVIDADE 1 - Ficha de pessoa
# Enunciado: crie um dicionário com nome, idade e cidade lidos do
# usuário. Mostre a ficha usando for com items().
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. criar dicionário vazio
#   2. ler nome, idade, cidade e guardar por chave
#   3. for k, v in items() -> imprimir

pessoa = {}
pessoa['nome'] = input('Nome: ')
pessoa['idade'] = int(input('Idade: '))
pessoa['cidade'] = input('Cidade: ')
for k, v in pessoa.items():
    print(f'{k}: {v}')


# ---------------------------------------------------------------------
# ATIVIDADE 2 - Média do aluno
# Enunciado: leia nome e média de um aluno. Guarde no dicionário e
# acrescente a chave 'situação': 'Aprovado' (média >= 7),
# 'Recuperação' (5 a 6.9) ou 'Reprovado' (< 5). Mostre tudo.
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. ler nome e média -> dicionário
#   2. if/elif/else sobre a média
#   3. criar a chave 'situação' com o resultado
#   4. imprimir com items()

aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


# ---------------------------------------------------------------------
# ATIVIDADE 3 - Contador de palavras
# Enunciado: dada a frase abaixo, conte quantas vezes cada palavra
# aparece. Resultado esperado: {'a': 2, 'casa': 2, 'é': 1, 'bonita': 1}
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. separar a frase em palavras (split)
#   2. para cada palavra: se já está no dicionário, soma 1;
#      senão, começa com 1
frase = 'a casa é bonita a casa'
contagem = {}
for palavra in frase.split():
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)
# Versão curta equivalente: contagem[palavra] = contagem.get(palavra, 0) + 1


# ---------------------------------------------------------------------
# ATIVIDADE 4 - Cadastro de jogadores (lista de dicionários)
# Enunciado: cadastre 3 jogadores (nome e gols). Guarde cada um como
# dicionário dentro de uma lista. No final mostre todos e quem fez
# mais gols.
# ---------------------------------------------------------------------
# Pseudocódigo:
#   1. lista vazia
#   2. repetir 3x: ler nome e gols -> dicionário -> append
#   3. percorrer a lista imprimindo cada jogador
#   4. achar o maior valor de 'gols'

jogadores = []
for c in range(3):
    jogador = {}
    jogador['nome'] = input(f'Nome do jogador {c + 1}: ')
    jogador['gols'] = int(input('Gols: '))
    jogadores.append(jogador)   # aqui o dicionário é recriado a cada volta, então não precisa de copy()

for j in jogadores:
    print(f"{j['nome']} fez {j['gols']} gols")

artilheiro = jogadores[0]
for j in jogadores:
    if j['gols'] > artilheiro['gols']:
        artilheiro = j
print(f"Artilheiro: {artilheiro['nome']} com {artilheiro['gols']} gols")


# ---------------------------------------------------------------------
# ATIVIDADE 5 (DESAFIO) - Dados de uma lista de números
# Enunciado: leia 5 números e monte UM dicionário com as chaves
# 'quantidade', 'soma', 'maior' e 'menor'. Mostre o dicionário.
# ---------------------------------------------------------------------
numeros = [int(input(f'Número {c + 1}: ')) for c in range(5)]
resumo = {
    'quantidade': len(numeros),
    'soma': sum(numeros),
    'maior': max(numeros),
    'menor': min(numeros),
}
print(resumo)


# =====================================================================
# RESUMO RÁPIDO (cola para revisar)
# d = {'chave': valor}      cria dicionário
# d['chave']                lê o valor (KeyError se não existir)
# d.get('chave', padrão)    lê sem dar erro
# d['nova'] = valor         adiciona (ou altera se já existir)
# del d['chave']            apaga
# d.keys() / .values() / .items()
# 'chave' in d              testa se a CHAVE existe
# for k, v in d.items():    percorre chave e valor
# b = a.copy()              copia de verdade (b = a só cria apelido)
# lista de dicionários      [{...}, {...}] -> lista[i]['chave']
# =====================================================================