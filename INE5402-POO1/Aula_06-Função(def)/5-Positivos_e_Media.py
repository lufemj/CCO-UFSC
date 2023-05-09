def media (total, x):
    m = total / x
    print (f"A média dos {x} valores positivos é de{m: 0.1f}.")
        

x = 0
total = 0

for i in range(0,6):
    n = float(input(f"Digite o {i+1}° valor: "))
    if n > 0:
        x += 1
        total += n

media (total, x)
