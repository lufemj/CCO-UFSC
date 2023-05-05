n = int(input("Quantas camisas serão sorteadas? "))

for i in range(n):
    qt, s = map(int, input("Informe a quantidade de alunos e o número secreto: ").split())
    valores = list(map(int, input("Informe os números dos grupos: ").split()))
    valores_proximos = []
    menor = 101

    for j in range(len(valores)):
        if valores[j] == s:
            valores_proximos.append(j+1)
            break
        else:
            aux = valores[j] - s
            if aux < 0:
                aux *= -1
            if aux < menor:
                menor = aux
                valores_proximos.append(j + 1)

    print(valores_proximos[-1])
