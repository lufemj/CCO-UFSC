import random

linha = [0] * 12
matriz = [linha] * 12

while True:
    lin = int(input("Qual linha deseja realizar a operação: "))
    lin -= 1
    if 0 <= lin < 12:
        break
    else:
        print("Erro. Digite novamente.")
        
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
        '''n = random.random()
        n = round(((n*100) / 10),2)'''
        n = int(input(f"Digite o número da linha {l} coluna {c}: "))
        linha.append(n)
    matriz[l] = linha

aux = 0

for c in range (12):
    aux +=  matriz[lin] [c]
        
if t == "M":
    print(round((aux/ 12),2))

elif t == "S":
    print (round((aux),2))


