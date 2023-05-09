def tempo(n):
    tfinal = 0
    t0 = 0
    tf = 0
    for i in range (1, n+1):
        tsensor = int(input(f"Tempo que a pessoa {i}° passou pelo sensor: "))
        if i == 1:
            t0 = tsensor

        if i == n:
            tf = tsensor

    tfinal = (tf - t0) + 10

    return tfinal

while True:
    n = int(input("Número de pessoas que o sensor detectou: "))
    if 1 <= n <= 1000:
        break
    else:
        print("Dados invalidos, digite novamente.")

tempo_total = tempo(n)
    
print(tempo_total)