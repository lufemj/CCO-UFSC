while True: 
    n, m = map(int,input("Informe o número de participantes e o número de problemas: ").split())
    
    if n == m == 0:
        break

    else:
        cond = 4
        lista = [0] * m
        resultados = []

        for o in range(n):
            dados = list(map(int,input("Informe 1 caso o competidor resolveu cada problema, e 0 caso contrário: ").split()))

            resultados.append(dados)

        for i in range(n):
            for j in range (m):
                if resultados[i][j] == 1:
                    lista[j] += 1
        if lista.count(0) > 0:
            cond -= 1

        for k in range(m):
            if lista[k] == n:
                cond -= 1
                break

        for l in range (n):
            aux = resultados[l].count(0)
            if aux == m:
                cond -= 1
                break

        for a in range (n):
            aux = aux = resultados[a].count(1)
            if aux == m:
                cond -= 1
                break

        print(cond)
        


        
