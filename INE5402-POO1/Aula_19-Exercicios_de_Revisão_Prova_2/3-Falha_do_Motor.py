n = int(input("Informe o numero de medidas do motor: "))
medidas = list(map(int,input("Informe as medicoes do motor: ").split()))
queda = 0

for i in range(1, n):
    if medidas[i] < medidas[i-1]:
        queda = i
        print(queda)
        break

if queda == 0:
    print(queda)

