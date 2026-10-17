valor = float(input("valor da casa?"))
salario = float(input("qual seu salário?"))
anos = int(input("quantos anos de financiamento?"))

mensal = valor / (anos * 12)
 
if mensal <= salario * 0.30:
    print(f"seu empréstimo será de R${mensal:.2f}")
else:
    print("seu empréstimo foi negado")