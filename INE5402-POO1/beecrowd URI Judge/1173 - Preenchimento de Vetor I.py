list = []
list.append(int(input("Informe o valor: ")))
n = 0
while n < 10:
    
    list.append((list[n])*2)

    print(f"N[{n}] = {list[n]}")
    n += 1
