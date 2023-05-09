n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = ((n1*2) + (n2*3) + (n3*4) + n4) / 10

if media >= 7.0:
    print(f"Média: {media: 0.1f}")
    print("Aluno Aprovado")
elif 6.9 > media > 5.0:
    print(f"Média: {media: 0.1f}")
    print("Aluno em Exame")

    n5 = float(input("Nota 5: "))
    media2 = (n5 + media) / 2

    if media2 > 5.0: 
        print(f"Nota do exame: {n5: 0.1f}")
        print("Aluno Aprovado")
        print(f"Média Final: {media2: 0.1f}")
    else:
        print(f"Nota do exame: {n5: 0.1f}")
        print("Aluno Reprovado")
        print(f"Média Final: {media2: 0.1f}")

else:
    print(f"Média: {media: 0.1f}")
    print("Aluno Reprovado")