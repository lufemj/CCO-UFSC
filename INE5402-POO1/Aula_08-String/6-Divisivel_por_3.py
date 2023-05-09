m, n = input("Informe o número de algarismos e um número: ")
x = len(n)
ntotal = 0

for i in range (x):
    y = int(n[i])

    ntotal += y

if (ntotal%3) == 0:
    divisivel = "Sim"
else:
    divisivel = "Não"

print(ntotal, divisivel)
