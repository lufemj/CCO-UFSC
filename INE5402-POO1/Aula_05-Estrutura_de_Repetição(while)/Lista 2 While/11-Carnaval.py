n = 1
maior = 0
menor = 10
total = 0

while n < 6:
    nota = float(input(f"Qual a nota {n}: "))

    if nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota

    total += nota

    n += 1

final = (total - menor - maior)

print(f"A nota final da escola de samba foi: {final: 0.1f}")