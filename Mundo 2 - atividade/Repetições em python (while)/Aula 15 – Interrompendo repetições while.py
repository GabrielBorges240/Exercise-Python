# ============================================================
# AULA 15 - Interrompendo repetições while
# Curso em Vídeo - Python (Gustavo Guanabara)
# Tópicos: break, loopings infinitos, f-strings
# ============================================================


# ------------------------------------------------------------
# 1) O QUE É O break?
# ------------------------------------------------------------
# O break é um comando que INTERROMPE o laço de repetição
# imediatamente, mesmo que a condição do while ainda seja
# verdadeira. Ele "quebra" o loop e o programa continua na
# primeira linha depois do while.
#
# É muito usado quando queremos parar a repetição no meio do
# caminho, por causa de alguma condição especial (ex: usuário
# digitou uma senha errada, encontrou o número procurado, etc).

# Exemplo simples:
contador = 0
while True:  # loop "infinito" de propósito
    contador += 1
    print(f'Contando {contador}')
    if contador >= 5:
        print('Chega! Vou parar o loop aqui.')
        break  # interrompe o while, mesmo sendo True


# ------------------------------------------------------------
# 2) LOOPINGS INFINITOS (while True)
# ------------------------------------------------------------
# Antes usávamos while <condição> para controlar quando parar.
# Agora vamos usar while True (que NUNCA é falso sozinho) e
# colocamos o break DENTRO do loop, na hora certa, para parar.
#
# Vantagem: o código fica mais organizado, pois a lógica de
# "quando parar" fica junto da lógica de "o que fazer", sem
# precisar controlar uma variável de condição só para isso.

# Exemplo: pedir um número até a pessoa digitar 0
while True:
    num = int(input('Digite um número (0 para sair): '))
    if num == 0:
        print('Você digitou 0. Encerrando o programa...')
        break
    print(f'Você digitou o número {num}.')


# ------------------------------------------------------------
# 3) F-STRINGS (formatted strings)
# ------------------------------------------------------------
# É uma forma moderna e mais fácil de formatar textos com
# variáveis dentro. Basta colocar um "f" antes das aspas e
# escrever as variáveis entre chaves {}.
#
# Antes:
nome = 'Maria'
idade = 25
print('Meu nome é {} e eu tenho {} anos.'.format(nome, idade))

# Com f-string (mais legível e direto):
print(f'Meu nome é {nome} e eu tenho {idade} anos.')

# f-strings também aceitam expressões dentro das chaves:
print(f'Ano que vem terei {idade + 1} anos.')

# E também formatação de casas decimais, alinhamento, etc:
preco = 49.9
print(f'O produto custa R$ {preco:.2f}')  # duas casas decimais


# ============================================================
# EXERCÍCIOS RESOLVIDOS
# ============================================================

# ------------------------------------------------------------
# Exercício 1
# Crie um programa que fique pedindo números ao usuário e
# mostre a soma total no final, quando ele digitar um valor
# negativo (usando while True + break).
# ------------------------------------------------------------
print('=== Exercício 1 ===')
soma = 0
while True:
    valor = float(input('Digite um número (negativo para parar): '))
    if valor < 0:
        break
    soma += valor
print(f'A soma dos números digitados foi {soma}')


# ------------------------------------------------------------
# Exercício 2
# Faça um jogo de adivinhação: o programa "pensa" em um número
# (fixo, para fins didáticos) e o usuário tenta adivinhar.
# O loop só para quando o usuário acertar (break).
# ------------------------------------------------------------
print('=== Exercício 2 ===')
numero_secreto = 7
tentativas = 0
while True:
    chute = int(input('Tente adivinhar o número secreto (1 a 10): '))
    tentativas += 1
    if chute == numero_secreto:
        print(f'Parabéns! Você acertou em {tentativas} tentativa(s)!')
        break
    elif chute < numero_secreto:
        print('O número secreto é maior. Tente novamente.')
    else:
        print('O número secreto é menor. Tente novamente.')


# ------------------------------------------------------------
# Exercício 3
# Crie um sistema de login simples: o usuário tem no máximo
# 3 tentativas para acertar a senha correta. Use break quando
# acertar, e f-strings para mostrar as mensagens.
# ------------------------------------------------------------
print('=== Exercício 3 ===')
senha_correta = '1234'
max_tentativas = 3
tentativa_atual = 0

while tentativa_atual < max_tentativas:
    senha = input('Digite a senha: ')
    tentativa_atual += 1
    if senha == senha_correta:
        print(f'Acesso liberado! (tentativa {tentativa_atual})')
        break
    else:
        restantes = max_tentativas - tentativa_atual
        if restantes > 0:
            print(f'Senha incorreta. Você tem {restantes} tentativa(s) restante(s).')
        else:
            print('Número máximo de tentativas atingido. Acesso bloqueado.')


# ------------------------------------------------------------
# Exercício 4
# Faça um programa que leia vários nomes até que a pessoa
# digite "sair". No final, mostre quantos nomes foram
# cadastrados, usando f-string.
# ------------------------------------------------------------
print('=== Exercício 4 ===')
nomes = []
while True:
    entrada = input('Digite um nome (ou "sair" para encerrar): ')
    if entrada.lower() == 'sair':
        break
    nomes.append(entrada)

print(f'Foram cadastrados {len(nomes)} nome(s): {nomes}')