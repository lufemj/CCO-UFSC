def movimento (x,y):
    menor_saldo = y
    while x > 0:
        movi = int(input("Qual o movimento de dinheiro? "))
        y += movi
        if y < menor_saldo:
            menor_saldo = y
        x -= 1
    print(f"O menor valor de saldo da conta no período dado foi de: {menor_saldo}")

ndias, saldoi = map(int,input("Informe o número de dias do período de interesse e o saldo da conta no início do período: ").split())

movimento (ndias, saldoi)