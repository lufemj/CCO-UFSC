n = int(input("Informe o numero inteiro: "))
seq = list(map(int,input("Informe a sequencia de numeros: ").split()))


seq.sort()

for i in range(len(seq)):
    if i+1 != seq[i]:
        print(i+1)
        break