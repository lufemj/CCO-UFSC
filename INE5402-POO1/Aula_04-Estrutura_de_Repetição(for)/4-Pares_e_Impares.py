NP = 0
NI = 0
for i in range(10):
    inteiro=int(input("Digite um número inteiro: "))
    if inteiro%2==0:
        NP=NP+1
    else:
        NI=NI+1
print(f"Números Pares: {NP}, Números ìmpares {NI}.")
    