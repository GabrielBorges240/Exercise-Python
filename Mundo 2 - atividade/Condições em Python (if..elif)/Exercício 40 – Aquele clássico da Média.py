nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("segunda nota:")) 
media = (nota1 + nota2) / 2
print(f"A média do aluno é: {media}")

if media < 5.0:
    print("\033[1;31m REPROVADO.\033[m")  
elif media >= 7.0:
    print("\033[1;32m APROVADO. \033[m") 
else:
    print("\033[1;33m RECUPERAÇÃO!\033[m")  
      