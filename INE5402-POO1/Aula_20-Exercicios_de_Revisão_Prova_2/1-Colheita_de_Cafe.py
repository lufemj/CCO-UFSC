while True:

    m, n = map(int,input("Informe o numero de linhas e colunas da matriz: ").split())

    matriz = [0] * m

    litros = 0

    print("Informe a matriz:")
    for i in range (m):
        valores = list(map(int,input().split()))
        matriz[i] = valores

    for l in range (m):
        for c in range(n):
            litros += matriz[l][c]

    sacas = litros // 60
    litros -= (sacas*60)

    print(f"{sacas} saca(s) e {litros} litro(s)")


    cont = input("Deseja continuar?  S/N ")
    if cont.upper() != "S":
        break