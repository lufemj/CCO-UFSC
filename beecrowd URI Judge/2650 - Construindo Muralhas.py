n, w = map(int,input("Informe o número de titãs e o tamanho da muralha: ").split())
marley = []
atravessam = []

for i in range (n):
    tita = input("Informe o nome do titã e sua altura: ").split()
    tita[2] = int(tita[2])

    marley.append(tita)

for j in range(n):
    if marley[j][2] > w:
        atravessam = marley[j][0:2]
        print(*atravessam)
