a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a+b > c and a+c > b and b+c > a:
    perimetro = a + b + c
    print(f"O perimetro do triângulo é: {perimetro}")
else:
    area = ((a+b) * c) / 2
    print(f"A área do trapézio é: {area}")