while True:
    n,c = input("Indique o número de leituras realizadas pelo sensor e a capacidade máxima do elevador, separados por espaço: ").split()
    n = int(n)
    c = int(c)
    if 1 <= n <= 1000 and 1 <= c <= 1000:
        break
    else:
        print("Dados invalidos, digite novamente.")

pessoas = 0
capacidade = "N"

for i in range(0,n):
    while True:
        s, e = input("Indique quantas pessoas saíram e quantas pessoas entraram neste andar: ").split()
        s= int(s)
        e = int(e)

        if 1 <= n <= 1000 and 1 <= c <= 1000:
            break
        else:
            print("Dados invalidos, digite novamente.")
    pessoas -= s
    pessoas += e
    if pessoas > c:
        capacidade = "S"

print(capacidade)

