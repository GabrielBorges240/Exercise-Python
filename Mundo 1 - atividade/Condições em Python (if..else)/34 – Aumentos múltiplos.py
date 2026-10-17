salario = float(input("Qual seu salário?"))
if salario <= 1250:    
   aumento = salario * 0.15

else:
   aumento = salario * 0.10
   print(f'seu aumento será R${aumento:.2f}') 
   print(f'seu novo salário será R${salario + aumento:.2f}')
 