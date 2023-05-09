while True:
    l, c, p = input().split()
    if l == c == p == 0:
        break

    l = int(l)
    c = int(c)
    p = int(p)

    matriz = [0] * l
    ventesq = 0
    ventdir = 0
    boom = 0

    print("Informe a matriz:")
    for i in range(l):
        aux = input().split()
        for j in range(len(aux)):
            aux[j] = int(aux[j])
        
        matriz[i] = aux

    for o in range(l):
        #Verificar a direita do balao
        for k in range((c-p)):
            if matriz[o][p+k] != 0:
                ventdir = matriz[o][p+k]
                break
        
        #Verificar a esquerda do balao
        for g in range(1,p+1):
            if matriz[o][p-g] != 0:
                ventesq = matriz[o][p-g]
                break
        
        if ventdir > ventesq:
            if (ventdir - ventesq) == p:
                print(f"BOOM {o} {ventdir+p}")
            else:
                p -= (ventdir - ventesq)
        elif ventdir < ventesq:
            if (ventesq - ventdir) == p:
                print(f"BOOM {o} {ventesq+p}")
            else:
                p -= (ventesq - ventdir)

    if boom == 0:
        print(f"OUT {p}")