import random

linha = [0] * 12
matriz = [linha] * 12

while True:
    t = input("Digite 'M' se  deseja realizar a média ou 'S' se deseja realizar a soma da linha: ")
    t = t.upper()
    if t == "S" or t == "M":
        break
    else:
        print("Erro. Digite novamente.")
        

for l in range (12):
    linha = []
    for c in range (12):
        n = random.random()
        n = round(((n*100) / 10),2)
        #n = int(input())
        linha.append(n)
    matriz[l] = linha


for linha in range (0,12):
    for coluna in range (0,12):
        print(f"[{matriz[linha] [coluna]:^5}]", end = "")
    print()
    
aux = 0
x = 0
for l in range (1,12):
    for c in range (l):
        aux += matriz[l][c]
        x += 1
        

#print(aux)
    


if t == "M":
    print(round((aux/ x),2))

elif t == "S":
    print (round((aux),2))
