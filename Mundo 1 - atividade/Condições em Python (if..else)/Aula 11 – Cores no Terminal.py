# === Guia rápido de cores ANSI ===
# Formato: \033[<estilo>;<cor_texto>;<cor_fundo>m
# Estilo:
#   0 = reset (padrão)
#   1 = negrito
#   4 = sublinhado
#   7 = inversão (swap cor texto/fundo)
#
# Cores de texto (30–37):
#   30 = preto
#   31 = vermelho
#   32 = verde
#   33 = amarelo
#   34 = azul
#   35 = magenta
#   36 = ciano
#   37 = branco
#
# Cores de fundo (40–47):
#   40 = preto
#   41 = vermelho
#   42 = verde
#   43 = amarelo
#   44 = azul
#   45 = magenta
#   46 = ciano
#   47 = branco
#
# Exemplo: \033[1;32;44m → texto verde em negrito com fundo azul

# Aula sobre cores no terminal usando ANSI
# O código \033[m é usado para controlar cores e estilos no terminal

print("\033[31mOlá, mundo em vermelho!\033[m")   # \033[31m ativa a cor vermelha
print("\033[32mTexto verde\033[m")               # \033[32m ativa a cor verde
print("\033[1;34mTexto azul em negrito\033[m")   # \033[1;34m combina negrito + azul
print("\033[7;33mTexto amarelo invertido\033[m") # \033[7;33m aplica efeito invertido

# Exemplos adicionais de cores e estilos ANSI

print("\033[1;31m[ERRO] Algo deu errado!\033[m")   # Vermelho em negrito → bom para mensagens de erro
print("\033[1;32m[SUCESSO] Operação concluída!\033[m") # Verde em negrito → bom para indicar sucesso
print("\033[1;33m[AVISO] Atenção ao próximo passo!\033[m") # Amarelo em negrito → usado como alerta
print("\033[1;36m[INFO] Processando dados...\033[m") # Ciano em negrito → mensagens informativas
print("\033[4;35mTexto roxo sublinhado\033[m")       # Magenta com sublinhado
print("\033[30;47mTexto preto com fundo branco\033[m") # Contraste forte
print("\033[1;37;41mTexto branco em negrito com fundo vermelho\033[m") # Destaque máximo


# 🌈 Mais exemplos de cores e estilos ANSI

print("\033[90mTexto cinza claro\033[m")          # Cinza claro
print("\033[1;90mTexto cinza escuro em negrito\033[m") # Cinza escuro em negrito
print("\033[1;94mTexto azul claro em negrito\033[m")   # Azul claro
print("\033[1;95mTexto magenta claro em negrito\033[m") # Magenta claro
print("\033[1;96mTexto ciano claro em negrito\033[m")   # Ciano claro

# 🎨 Fundos coloridos
print("\033[37;44mTexto branco com fundo azul\033[m")
print("\033[30;42mTexto preto com fundo verde\033[m")
print("\033[33;45mTexto amarelo com fundo magenta\033[m")
print("\033[36;41mTexto ciano com fundo vermelho\033[m")

# ✨ Efeitos adicionais
print("\033[5;32mTexto verde piscando\033[m")     # Piscar (nem todos terminais suportam)
print("\033[2;37mTexto branco apagado\033[m")     # Texto "apagado" (dim)
print("\033[1;4;93mTexto amarelo em negrito e sublinhado\033[m")
print("\033[3;94mTexto azul em itálico\033[m")    # Itálico (suporte varia)


# Lista de códigos ANSI para cores (você pode expandir)
cores = [
    "\033[31m",  # vermelho
    "\033[32m",  # verde
    "\033[33m",  # amarelo
    "\033[34m",  # azul
    "\033[35m",  # magenta
    "\033[36m",  # ciano
    "\033[91m",  # vermelho claro
    "\033[92m",  # verde claro
    "\033[93m",  # amarelo claro
    "\033[94m",  # azul claro
    "\033[95m",  # magenta claro
    "\033[96m",  # ciano claro
]

frase = "Colorindo cada letra!"
resultado = ""

for i, letra in enumerate(frase):
    cor = cores[i % len(cores)]  # alterna entre as cores
    resultado += f"{cor}{letra}\033[m"

print(resultado)
