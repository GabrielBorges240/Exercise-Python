from math import radians, sin, cos, tan 

angulo  = float(input("Digite um angulo:")) 

se = sin(radians(angulo))
co = cos(radians(angulo))
ta = tan(radians(angulo))

print(f"O valor do seno é: {se:.2f}")
print(f"O valor do cosseno é: {co:.2f}")
print(f"O valor da tangente é: {ta:.2f}")

#sin - seno
#cos - cosseno
#tan - tangente