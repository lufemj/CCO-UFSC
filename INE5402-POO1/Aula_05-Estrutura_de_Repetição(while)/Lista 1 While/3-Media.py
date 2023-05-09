from cmath import inf

x = 1
seq = True
soma = 0
maior = 0
menor = inf

while seq:
    num = int(input("Digite o número: "))
    soma = soma + num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    cont = input("Continuar a digitar valores? S/N: ")
    if cont == "S":
        x += 1
    else:
        seq = False

media = soma / x

print(f"A média foi {media}. O maior valor lido foi {maior}, e o menor foi {menor}.")