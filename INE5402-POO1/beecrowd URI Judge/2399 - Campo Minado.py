while True:
    t=int(input("Indique o número de células no tabuleiro: "))
    aux = t
    if 1 <= t <= 50:
        break
    else:
        print("Erro. Digite novamente.")

while t != 0:
        
    n = t

    list=[]

    for i in range(0,n):
        m=int(input("Informe 0 se não existe mina e 1 se existe uma mina: "))
        list.append(m)

    for j in range(0,n):
        if j==0 and n>1:
            print(list[j]+list[j+1])
        elif j==n-1:
            print(list[j-1]+list[j])
        else:
            print(list[j-1]+list[j]+list[j+1])
    t -= 1