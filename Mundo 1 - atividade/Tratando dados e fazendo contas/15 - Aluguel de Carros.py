alugado = int(input("Por quantos dias o carro foi alugado?"))
km = float(input("Quantos km foram percorridos?"))

preco = (alugado * 60) + (km * 0.15)

print(f"O preço a pagar é: R${preco}")