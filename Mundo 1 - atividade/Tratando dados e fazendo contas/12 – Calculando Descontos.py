preço = float(input('Qual o preço do produto?'))
desconto = preço * 0.05
preço_final = preço - desconto

print(f'O preço final do produto com desconto de 5% é: R${preço_final:.2f}')