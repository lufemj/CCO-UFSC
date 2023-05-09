while True:
    n = int(input("Informe o número de casos: "))
    if 1 <= n <= 20:
        break
    else:
        print("Erro. Digite novamente.")

for i in range (n):
    aux = 0
    list = []

    while True:
        x = int(input("numero: "))
        if 1 <= n <= (10**8):
            break
        else:
            print("Erro. Digite novamente.")
    

    for j in range (1, x):
        if (x%j) == 0:
            list.append(j)

    for k in range (len(list)):
        aux += list[k]

    if aux == x:
        print(f"{x} é perfeito")
    else: 
        print(f"{x} não é perfeito")