n = int(input("Dê o valor de um número: "))
x = 1

while x <= 10000:
    if x % n == 2:
        print (x)
    x += 1