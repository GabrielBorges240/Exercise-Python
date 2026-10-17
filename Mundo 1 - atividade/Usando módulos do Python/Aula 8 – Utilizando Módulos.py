# -----------------------------
# MÓDULOS EM PYTHON
# -----------------------------
# Módulos são bibliotecas de funções prontas que ampliam os recursos do Python.
# Podem ser:
# - Built-in (já vêm com o Python, ex: math, random, datetime)
# - Externos (instalados via PyPI com pip install)

# -----------------------------
# IMPORTANDO MÓDULOS
# -----------------------------
# import - carrega o módulo inteiro
import math
print(math.sqrt(25))  # raiz quadrada

# from/import - importa apenas funções específicas
from math import sqrt, ceil
print(sqrt(25))   # raiz quadrada
print(ceil(4.2))  # arredonda para cima

# as - cria um apelido para o módulo
import math as m
print(m.sqrt(9))  # raiz quadrada usando apelido

# -----------------------------
# MÓDULOS BUILT-IN
# -----------------------------
# math - funções matemáticas
print(math.factorial(5))  # fatorial de 5

# random - gera números aleatórios
import random
print(random.randint(1, 10))  # número aleatório entre 1 e 10

# datetime - manipulação de datas
import datetime
print(datetime.date.today())  # data atual

# -----------------------------
# MÓDULOS EXTERNOS (PyPI)
# -----------------------------
# Para instalar módulos externos:
# pip install nome_do_modulo
# Exemplo: pip install requests

# requests - para fazer requisições HTTP
import requests
resposta = requests.get("https://www.google.com")
print(resposta.status_code)  # código da resposta (200 = OK)

# -----------------------------
# DOCUMENTAÇÃO E AJUDA
# -----------------------------
# help() - mostra funções disponíveis em um módulo
help(math)  # lista todas as funções do módulo math
