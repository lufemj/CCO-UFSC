n = 1
m = 1
aux = 0

while n > 0 and m > 0:
    total = 0
    n = int(input("Dê o valor de um número N: "))
    m = int(input("Dê o valor de um número M: "))
    if n <= 0 or m <= 0:
        break

    if n > m:
        aux = n
        n = m
        m = aux

    while n <= m:
        total += n
        print(n)
        n += 1
    
    print(f"Soma = {total}")