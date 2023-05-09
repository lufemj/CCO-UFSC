import math

x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"A distância entre os dois pontos é: {distancia: 0.4f}")