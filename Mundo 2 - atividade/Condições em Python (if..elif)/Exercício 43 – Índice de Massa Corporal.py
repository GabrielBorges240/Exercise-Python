# -*- coding: utf-8 -*-
massa = float(input("Digite sua massa em kg:"))
altura = float(input("Digite sua altura em metros:"))

imc = massa / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com o peso ideal.")    
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
elif 30 <= imc < 40:    
    print("Você está com obesidade.")
else: 
    print("Você está com obesidade mórbida.")    
 