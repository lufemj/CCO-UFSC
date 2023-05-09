l = float(input("Dê a largura da caixa: "))
a = float(input("Dê a altura da caixa: "))
p = float(input("Dê a proundidade da caixa: "))
r = float(input("Dê o raio da esfera: "))

if l**2 + a**2 + p**2 <= 4*r**2:
    print("S")
else:
    print("N")