A = float(input("Digite o valor A: "))
B = float(input("Digite o valor B: "))
C = float(input("Digite o valor C: "))
pi = 3.14159

atriangulo = (A * C) / 2

acircurlo = pi * (C**2)

atrapezio = ((A + B) * C) / 2

aquadrado = B**2

aretangulo = A * B

print(f"Triangulo: {atriangulo: 0.3f}, Circulo: {acircurlo: 0.3f}, Trapezio: {atrapezio: 0.3f}, Quadrado: {aquadrado: 0.3f}, Retangulo: {aretangulo: 0.3f}")