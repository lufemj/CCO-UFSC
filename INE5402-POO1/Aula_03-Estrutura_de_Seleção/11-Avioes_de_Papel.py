c = int(input("Número de competidores: "))
p = int(input("Número de folhas de papel: "))
f = int(input("Número de folhas para cada competidor: "))

if (p/c) >= f:
    print ("S")
else:
    print("N")