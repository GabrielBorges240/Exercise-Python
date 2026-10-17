valor_saque = int(input('número inteiro'))

total = valor_saque

cedulas = [50, 20, 10, 1]
notas_entregues =  0
i = 0
while i < len(cedulas):
       cedula = cedulas[i]
       if total >= cedula:
            quantidade = total // cedula
            total = total % cedula
            notas_entregues = notas_entregues + quantidade

            if quantidade > 0:
                print(f'{quantidade} nota(s) de R$ {cedula}')
       i = i + 1
       
print("Total de notas entregues:", notas_entregues)
