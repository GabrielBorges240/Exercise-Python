km = float(input("Quantos km foram percorridos?")) 
if km > 80: 
   multa = (km - 80) * 7
   print(f"voce ultrapassou o limite! multa vai custar R${multa:.2f}")
else:
   print('velocidade dentro do limite')  
 
