while True:    
    n = int(input("Informe a quantidade de numeros: "))
    if n == 0:
        break

    a = list(map(int,input("Informe os numeros: ").split()))
    a.sort()

    for i in range(0,(len(a)),2):
        if i+1 >= len(a):
            print(a[i])
            break
        elif a[i] != (a[i+1]):
            print(i+1)