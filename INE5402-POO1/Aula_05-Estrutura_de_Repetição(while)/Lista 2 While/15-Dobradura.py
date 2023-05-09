x = True
d = 9
teste = 1

while x:
    n = int(input("Quantas operações de dobraduras irão ser realizadas? "))
    if n == -1:
        break
    n = n * d
    if n == 0:
        n = 4
    print(f"Teste {teste}")
    print(f"Pedaços de papel: {n}")
    print()
    teste += 1
    