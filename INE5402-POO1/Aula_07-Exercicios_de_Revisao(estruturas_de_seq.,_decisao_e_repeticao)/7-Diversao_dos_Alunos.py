def jogo(n,m):
    while n > 0:
        primo1 = False
        s = 0
        for i in range(1, n+1):
            aux = n % i
            if aux == 0:
                s += 1
        if s == 2:
            primo1 = True
            
        if primo1:
            break
        else:
            n -= 1

    while m > 0:
        primo2 = False
        z = 0
        for i in range(1, m+1):
            auxx = m % i
            if auxx == 0:
                z += 1
        if z == 2:
            primo2 = True
            
        if primo2:
            break
        else:
            m -= 1

    print(f"A multiplicacão de P1 e P2 é: {n*m}")

n = int(input("Número de Juilherme: "))
m = int(input("Número de Jogério: "))

jogo(n,m)


