km = float(input("Qual a distância da viagem em Km?"))
if km <= 200:  
   preco = km * 0.50   
else:
   preco = km * 0.45
   print(f"O preço da passagem será R${preco:.2f}") 
 