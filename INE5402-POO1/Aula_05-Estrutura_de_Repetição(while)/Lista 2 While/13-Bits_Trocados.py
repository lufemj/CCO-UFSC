x = True
while x:
    v = int(input("Valor monetário: "))
    if v == 0:
        break
    cinquenta = 0
    vinte = 0
    dez = 0
    cinco = 0
    um = 0
    while v != 0:
        if (v - 50) >= 0:
            v -= 50
            cinquenta += 1
        elif (v - 10) >= 0:
            v -= 10
            dez += 1
        elif (v - 5) >= 0:
            v -= 5
            cinco += 1
        elif (v - 1) >= 0:
            v -= 1
            um += 1
    print(f"A converção do valor foi para {cinquenta} nota(s) de B$50, {dez} nota(s) de B$10,00, {cinco} nota(s) de B$5,00 e {um} nota(s) de B$1,00.")