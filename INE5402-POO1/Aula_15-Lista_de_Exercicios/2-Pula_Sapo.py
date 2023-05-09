while True:
    p, n = map(int,input("Informe a altura do pulo do sapo e o número de canos: ").split())
    p, n = map(int,input("Informe a altura do pulo do sapo e o número de canos: ").split())

    if (1 <= p <= 5) and (2 <= n <= 100):
        break
    else:
        print("Erro. Digite novamente.")

x = 0 

while True:
    canos = list(map(int,input("Informe as alturas dos canos ordenados da esquerda para a direita: ").split()))
    for j in range (len(canos)):
        if canos[j] > 10:
            print("Não pode haver canos com altura maior que 10. Digite Novamente.")
            x = 1
            break
    if x == 0:
        break
    
y = 0

for i in range ((n-1)):
    aux = canos[i] - canos[i+1]
    if aux < 0:
        aux *= -1

    if aux > p:
        print ("GAME OVER")
        y = 1
        break

if y == 0:
    print ("YOU WIN")