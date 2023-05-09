def media (nota, n, soma, maior):
    if nota > maior:
        maior = nota
        almaior = i+1

    media = soma / n

    return media, almaior, maior

n = int(input("Infome quantas notas serão calculadas: "))
soma = 0
maior = 0


for i in range(n):
    nota = int(input("Digite o número: "))
    soma += nota
    mediat, amnota, mnota = media (nota, n, soma, maior)

if mnota >= 5.75:
    status = "Aprovado"
elif mnota >= 2.75:
    status = "Em Recuperação"
else:
    status = "Reprovado"

print(mediat, amnota)
print(f"A média da turma foi {mediat: 0.2f}. A maior nota registrada foi {mnota}, do {amnota}° aluno {amnota}°, que ficou com o status {status}.")