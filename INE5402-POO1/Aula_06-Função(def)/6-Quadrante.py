def quadrante (x, y):
    if (x > 0 and y > 0):
        print("Primeiro Quadrante")
    elif (x < 0 and y > 0):
        print("Segundo Quadrante")
    elif (x < 0 and y < 0):
        print("Terceiro Quadrante")
    elif (x > 0 and y < 0):
        print("Quarto Quadrante")
    else:
        print("Entre Quadrantes")

x,y = input("Digite as coordenadas X e Y: ").split()
x = int(x)
y = int(y)


quadrante (x, y)
