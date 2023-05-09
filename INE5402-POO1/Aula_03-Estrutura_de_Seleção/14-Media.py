nota1 = float(input("Nota 1 do Aluno: "))
nota2 = float(input("Nota 2 do Aluno: "))
nota3 = float(input("Nota 3 do Aluno: "))

media = (nota1+nota2+nota3)/3

if media < 5:
    print("Aluno Reprovado")
    print(f"Média: {media: .2f}")
elif media < 7:
    print("Aluno em Recuperação")
    print(f"Média: {media: .2f}")
else :
    print("Aluno Aprovado")
    print(f"Média: {media: .2f}")