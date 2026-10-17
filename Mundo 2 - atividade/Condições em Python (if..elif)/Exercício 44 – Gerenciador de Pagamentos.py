produto = float(input("Preço das compras:"))

print("Escolha a forma de pagamento:")
print("1 - à vista dinheiro/cheque")
print("2 - à vista no cartão")
print("3 - 2x no cartão")
print("4 - 3x ou mais no cartão")

opcao = int(input("sua opção:"))
 
if opcao == 1:
    preço_final = produto  * 0.90 
    print(f"sua compra será à vista com 10% de desconto, totalizando R${preço_final:.2f}")

elif opcao == 2:
    preço_final = produto  * 0.95  
    print(f"sua compra será à vista no cartão com 5% de desconto, totalizando R${preço_final:.2f}") 

elif opcao == 3:
    parcelas = int(input("Quantas parcelas (até 2x)?"))
    if parcelas < 1 or parcelas > 2:
        print("Número de parcelas inválido para esta opção.")
    else:
        preço_final = produto
        print(f"sua compra será parcelada em {parcelas}x de R${preço_final / parcelas:.2f} sem juros, totalizando R${preço_final:.2f}")

elif opcao == 4:
    parcelas = int(input("Quantas parcelas (3x ou mais)? "))
    if parcelas < 3:
        print("Número de parcelas inválido para esta opção.")
    else:
        preço_final = produto * 1.20
        print(f"sua compra será parcelada em {parcelas} vezes de R${preço_final / parcelas:.2f} com 20% de juros, totalizando R${preço_final:.2f}")
else:
    print("Opção inválida de pagamento.")
    
