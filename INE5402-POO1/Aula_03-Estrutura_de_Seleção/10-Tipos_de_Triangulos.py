a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))
x = 0

if c >= b >= a:
    x = c
    c = a
    a = x
elif b >= a >= c:
    x = a
    a = b
    b = x
elif a >= c >= b:
    x = b
    b = c
    c = x
elif b >= c >= a:
    x = c 
    c = a
    a = b
    b = x
elif c >= a >= b:
    x = a 
    a = c
    c = b
    b = x

if a >= b+c:
    print("Não Forma Triângulo")
elif a**2 == (b**2 + c**2):
    print("Triângulo Retângulo")
elif a**2 > (b**2 + c**2):
    print("Triângulo Obtusângulo")
elif a**2 < (b**2 + c**2):
    print("Triângulo Acutângulo")

if a == b == c:
    print("Triângulo Equilatero")
elif (a == b) or (b == c) or (a == c):
    print("Triângulo Isósceles")