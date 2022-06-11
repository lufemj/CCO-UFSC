n = int(input("Indique o número de casos: "))
c = 0
r = 0
s = 0
total = 0

for i in range (n):
    while True:
        q, t = input("Informe a quantidade e o tipo de cobaia: ").split()
        t = t.upper()
        q = int(q)

        if 1 <= q <= 15 and (t == "C" or t == "R" or t == "S"):
            break
        else:
            print("Dados invalidos, digite novamente.")

    if t == "C":
        c += q
        total += q
    elif t == "R":
        r += q
        total += q
    elif t == "S":
        s += q
        total += q

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {((c/total)*100): 0.2f}%")
print(f"Percentual de ratos: {((r/total)*100): 0.2f}%")
print(f"Percentual de sapos: {((s/total)*100): 0.2f}%")