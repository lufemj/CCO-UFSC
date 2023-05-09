n, m = map(int,input("Informe o número de pedras e sapos: ").split())

list = []
for i in range (n):
    list.append(0)
  
for j in range (m):

    p, d = map(int,input("Informe a posição inicial do sapo e distância do pulo: ").split())
    
    list[p-1] = 1
    y = p + d - 1
    if y > (len(list)-1):
        x = y - n
        list[x] = 1
    else:
        list[y] = 1
    if d > len(list) - d:
        list[0] = 1



for k in range (n):
    print(list[k])