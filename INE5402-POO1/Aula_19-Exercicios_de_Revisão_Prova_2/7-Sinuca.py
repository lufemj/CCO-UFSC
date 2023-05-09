n = int(input("Informe o numero de bolas: "))


bolas = input("Informe as cores das bolas [-1 - branca] [1 - preta]: ").split()
for i in range(len(bolas)):
    bolas[i] = int(bolas[i])

while n > 1:
    plbolas = []

    for j in range(len(bolas)-1):
        if bolas[j] == bolas[j+1]:
            plbolas.append(1)
        else:
            plbolas.append(-1)

    bolas = plbolas
    n -=1

if bolas[0] == -1:
    print('branca')
if bolas[0] == 1:
    print('preta')
