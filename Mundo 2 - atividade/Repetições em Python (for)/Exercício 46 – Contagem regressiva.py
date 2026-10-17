from time import sleep  # Importa a função sleep do módulo time
print("Contagem regressiva para o lançamento do foguete")
for Contagem in range(10, -1, -1):  # Contagem regressiva de 10 até 0
    print(Contagem)           
    sleep(1)  # Pausa de 1 segundo entre cada número
print("lançamento!") 
print() 
        