# -----------------------------
# STRING - sequência de caracteres
frase = "Curso em Vídeo Python"

# -----------------------------
# ANÁLISE
# -----------------------------
# len() - conta quantos caracteres existem
print(len(frase))  # 21

# count() - conta quantas vezes aparece um caractere ou substring
print(frase.count("o"))  # 3

# find() - mostra a posição onde começa uma substring (ou -1 se não existir)
print(frase.find("Vídeo"))  # 6

# operador in - verifica se uma palavra existe dentro da string
print("Curso" in frase)  # True
print("Java" in frase)   # False

# -----------------------------
# TRANSFORMAÇÕES
# -----------------------------
# replace() - substitui uma palavra por outra
print(frase.replace("Python", "Java"))  # Curso em Vídeo Java

# upper() - transforma tudo em maiúsculas
print(frase.upper())  # CURSO EM VÍDEO PYTHON

# lower() - transforma tudo em minúsculas
print(frase.lower())  # curso em vídeo python

# capitalize() - só a primeira letra maiúscula
print(frase.capitalize())  # Curso em vídeo python

# title() - primeira letra de cada palavra maiúscula
print(frase.title())  # Curso Em Vídeo Python

# -----------------------------
# ESPAÇOS
# -----------------------------
frase2 = "   Olá Mundo   "

# strip() - remove espaços extras no início e no fim
print(frase2.strip())  # Olá Mundo

# rstrip() - remove espaços da direita
print(frase2.rstrip())  # "   Olá Mundo"

# lstrip() - remove espaços da esquerda
print(frase2.lstrip())  # "Olá Mundo   "

# -----------------------------
# DIVISÃO E JUNÇÃO
# -----------------------------
# split() - divide a string em lista de palavras
print(frase.split())  # ['Curso', 'em', 'Vídeo', 'Python']

# join() - junta elementos de uma lista em uma string
palavras = ["Python", "é", "legal"]
print(" ".join(palavras))  # Python é legal

# -----------------------------
# VERIFICAÇÕES
# -----------------------------
# startswith() - verifica se começa com determinada palavra
print(frase.startswith("Curso"))  # True

# endswith() - verifica se termina com determinada palavra
print(frase.endswith("Python"))  # True

# -----------------------------
# EXERCÍCIOS DA AULA
# -----------------------------
# Ex. 22 → Analisador de texto (contar letras, verificar posições)
# Ex. 23 → Separar dígitos de um número (unidade, dezena, centena, milhar)
# Ex. 24 → Verificar se a cidade começa com “Santo”
# Ex. 25 → Verificar se “Silva” está no nome
# Ex. 26 → Encontrar primeira e última ocorrência de uma letra
# Ex. 27 → Mostrar primeiro e último nome de uma pessoa
