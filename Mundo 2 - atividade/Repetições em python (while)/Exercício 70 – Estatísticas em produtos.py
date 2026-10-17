total_gasto_na_compra = 0
produto_mais_barato =  None
produto_mais_caro = None
name_produto_mais_barato = ""
name_produto_mais_caro = ""

while True:
    produto =  input("Digite o nome do produto: ")
    if not produto.isalpha():
        print("Produto inválido. Digite apenas letras.")
        continue
    preco = float(input("Digite o preço do produto: R$ "))
    total_gasto_na_compra += preco

    if produto_mais_barato is None or preco < produto_mais_barato:
        produto_mais_barato = preco
        name_produto_mais_barato = produto

    if produto_mais_caro is None or preco > produto_mais_caro:
        produto_mais_caro = preco
        name_produto_mais_caro = produto

    elif preco == produto_mais_caro:
        print(f"O produto {produto} tem o mesmo preço do produto mais caro.")

    continue_input = input("Deseja continuar cadastrando pessoas? (S/N): ").strip().upper()
    if continue_input == "N":
            break
     
print(f"Total gasto na compra: R$ {total_gasto_na_compra:.2f}")
print(f"Nome e preço do produto mais barato: {name_produto_mais_barato}, R$ {produto_mais_barato:.2f}")
print(f"Nome e preço do produto mais caro: {name_produto_mais_caro}, R$ {produto_mais_caro:.2f}")