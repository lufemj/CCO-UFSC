w = True

while w:
    x = int(input("Dê o valor do número X: "))
    y = int(input("Dê o valor do número Y: "))
    if x == y:
        break

    if y > x:
        print("Crescente")
    else:
        print("Decrescente")