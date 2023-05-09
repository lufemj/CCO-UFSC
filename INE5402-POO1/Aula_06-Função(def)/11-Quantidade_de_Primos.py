def primos (n, m):
    p = 0
    while n <= m:
        s = 0
        for i in range (n+1, 0, -1):
            x = n%i

            if x == 0:
                s += 1
        if s==2 :
            p +=1
        n += 1
    return p

        
    

n,m = map(int,input("Digite um intervalo de dois números: ").split())

nprimos = primos (n, m)

print(f"Existem {nprimos} primos entre {n} e {m}.")