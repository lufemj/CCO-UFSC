q=int(input(f"Informe o número de pessoas que participaram da pesquisa: "))
s=0
i=0

pesquisa = list(map(int,input().split("Informe a opinão dos entrevistados: ")))
for x in range (q):
    if pesquisa[x] == 0:
        s += 1
    else:
        i += 1

if i >= s:
    print("N")

else:
    print("Y")
