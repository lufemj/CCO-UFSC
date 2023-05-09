a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))

if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a%2 == 0:
    print("Valores aceitos")
else:
    print("Valores não aceitos")
