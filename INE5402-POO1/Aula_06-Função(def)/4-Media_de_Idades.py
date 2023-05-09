def media (itotal, n):
    m = itotal / n
    print (f"A média das idades é de{m: 0.2f} anos.")
        

x = True
itotal = 0
n = 0

while x:
    i = int(input(f"Digite a idade do indivíduo {n+1}: "))
    if i < 0:
        break
    else:
        itotal += i
        n += 1

media (itotal, n)
