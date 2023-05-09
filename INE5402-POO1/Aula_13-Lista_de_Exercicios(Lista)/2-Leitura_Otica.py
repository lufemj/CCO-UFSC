while True:
    n = int(input("Informe o número de casos: "))
    if 0 <= n <= 255:
        break
    else:
        print("Erro. Digite novamente.")

for i in range (n):
    dados = []
    gabarito = ["A", "B", "C", "D", "E"]
    menor = 127
    x = 0
    er = 0

    dados = list(map(int, input("Informe os valores lidos: ").split()))
        
    for k in range(len(dados)):
        if dados[k] <= menor:
            menor = dados[k]
            pos = k
        if dados[k] < 127:
            x += 1
    
    if x > 1:
        print("*")
    else:
        print(gabarito[pos])

