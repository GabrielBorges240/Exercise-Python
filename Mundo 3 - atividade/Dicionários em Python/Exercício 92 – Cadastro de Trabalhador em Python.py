from datetime import date
dados = {}
CTPS = 0

dados["nome"] = input("Seu Nome: ")
dados["nascimento"] = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
dados["idade"] = ano_atual - dados["nascimento"]
dados["CTPS"] = int(input("Sua Carteira Trabalho: "))


if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: R$ "))
    idade = ano_atual - dados["nascimento"]
    anos_faltando = (dados["Contratação"] + 35) - ano_atual
    dados["Aposentadoria"] = idade + anos_faltando
   
else:
    print('Não tem CTPS')
   
   