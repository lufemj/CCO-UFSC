list = []
for i in range(10):
    
    list.append(int(input("Informe o valor: ")))

    if list[i] <= 0:
        list[i] = 1
        
    print(f"X[{i}] = {list[i]}")
    
