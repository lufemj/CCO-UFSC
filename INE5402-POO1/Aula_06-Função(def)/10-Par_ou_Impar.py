def paridade (n):
    par = 0

    if n % 2 == 0:
        par = 1
    else:
        par = 0
    return par

num_par = 0

num_impar = 0

for i in range (10):
    n = int(input(f"Digite o {i+1}° número: "))

    npar = paridade (n)

    if npar == 1:
        num_par += 1
    else:
        num_impar += 1

print(f"Foram digitados {num_par} números pares e {num_impar} números ímpares.")