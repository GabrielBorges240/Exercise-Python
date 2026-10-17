from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento:"))
 
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")

if idade <= 9:
    print("Você é MIRIM.")
elif idade <= 14:
    print("Você é INFANTIL.") 
elif idade <= 19:
    print("Você é JÚNIOR.")
elif idade <= 25:
    print("Você é SÊNIOR.")    
else:
    print("Você é MASTER.")  
  
     