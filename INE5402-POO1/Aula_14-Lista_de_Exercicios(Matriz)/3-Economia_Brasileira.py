q=int(input(f"Número de pessoas que participaram da pesquisa: "))
pesquisa=list()
y=0
n=0
while 4 <= q <= 233000:
    pesquisa = input().split(" ")
    for X in range (q):
        if pesquisa[X] == "0":
            y+=1
        elif pesquisa[X] == "1":
            n+=1
        else:
            print("ERRO")
            break

    if n>=y:
        print("N")
        break
    elif n<y:
        print("Y")
        break