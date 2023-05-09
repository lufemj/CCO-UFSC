x = int(input("Dê o valor do número X: "))
y = int(input("Dê o valor do número Y: "))
volta = 0
sobra = 0
total = 0

if x > y:
        aux = x
        x = y
        y = aux

while total < x:
    total += sobra
    volta += 1
    sobra = y - x

print(f"Será ultrapassado na volta {volta}.")