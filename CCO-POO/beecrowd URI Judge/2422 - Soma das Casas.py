n = int(input("Informe o número de casas: "))
casa = []
for o in range(n):
    num = int(input(f"Informe o número da casa {o+1}: "))

    casa.append(num)

soma = int(input("Informe a soma dos números das casas com brinquedo escondido: "))

for i in range(n):
    for j in range(n):
        result = casa[i] + casa[j]
        if result == soma:
            break  
    if result == soma:
            break

print(casa[i], casa[j])