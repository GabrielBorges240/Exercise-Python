comprimento1 = float(input("primeiro segmento:"))
comprimento2 = float(input("segundo segmento:"))
comprimento3 = float(input("terceiro segmento:"))

if (comprimento1 < comprimento2 + comprimento3 and
    comprimento2 < comprimento1 + comprimento3 and
    comprimento3 < comprimento1 + comprimento2):
    print("Os segmentos acima PODEM formar um triângulo!")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")