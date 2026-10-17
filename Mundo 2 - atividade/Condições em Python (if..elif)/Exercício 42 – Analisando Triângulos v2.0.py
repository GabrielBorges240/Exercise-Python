equilatero  = float(input("primeiro segmento:"))
isoceles = float(input("segundo segmento:"))
escaleno = float(input("terceiro segmento:"))
 
if (equilatero < isoceles + escaleno and
    isoceles < equilatero + escaleno and
    escaleno < equilatero + isoceles):
    if equilatero == isoceles == escaleno:
        print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO!')
    elif equilatero == isoceles or isoceles == escaleno or escaleno == equilatero:
        print('Os segmentos acima PODEM formar um triângulo ISÓSCELES!')
    else:
        print('Os segmentos acima PODEM formar um triângulo ESCALENO!')
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")