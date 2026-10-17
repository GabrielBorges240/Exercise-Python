inteiro = int(input("digite um número inteiro:")) 

print('''escolher um base para conversão: 
[0] binário
[1] octal
[2] hexadecimal''')

opcao = int(input("sua opção:"))

if opcao == 0:
  print(f"o número {inteiro} em binário é {bin(inteiro) [2:]}")
elif opcao == 1:
    print(f"o número {inteiro} em octal é {oct(inteiro) [2:]}")
elif opcao == 2:
    print(f"o número {inteiro} em hexadecimal é {hex(inteiro) [2:]}")
else:
    print("opção inválida")