n = int(input("Quantos casos? "))
aux = 0


while n > 0:
    total = 0
    x = int(input("Dê o valor do número X: "))
    y = int(input("Dê o valor do número Y: "))
    
    if x > y:
        aux = x
        x = y
        y = aux

    x += 1
    while x < y:
        if x%2 != 0:
            total += x
        x += 1
    
    print(total)
    n -= 1