def tempo(n):
    tfinal = 0
    t0 = 0
    for i in range (1, n+1):
        tsensor = int(input(f"Tempo que a pessoa {i}° passou pelo sensor: "))
        if i == 1:
            t0 = tsensor
        else:
            t = tsensor - t0
            if t>= 10:
                tfinal = tfinal + 10
        t0 = t

    tfinal += 10

    print(tfinal)




while True:
    n = int(input("número de pessoas que o sensor detectou: "))
    if 1 <= n <= 1000:
        break
    else:
        print("Dados invalidos, digite novamente.")

tempo(n)
    