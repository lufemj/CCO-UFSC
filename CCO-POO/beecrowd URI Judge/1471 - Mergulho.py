while True:
    try:
        n, r = map(int,input("Informe o número de voluntários que mergulhou e o número de voluntários que retornou do mergulho: ").split())
        retonaram = list(map(int,input("Informe os mergulhadores que retornaram: ").split()))
        mergulhadores = []

        for i in range (1, n+1):
            mergulhadores.append(i)

        x = set(retonaram)
        y = set(mergulhadores)

        z = y.difference(x)

        if z == set():
            print("*")
        else:
            z = list(z)
            print (*z)
    except EOFError:
        break