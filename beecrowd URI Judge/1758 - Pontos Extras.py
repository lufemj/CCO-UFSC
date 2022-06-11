t = int(input("Indique a quantidade de casos de teste: "))

for e in range (t):
    medias = []
    p, n = map(int,input(f"Indique a quantidade de provas e a quantidade de alunos do caso {e+1}: ").split())
    
    for i in range(n):
        somanotas = 0
        maiornota10 = 0
        maiornota7 = 0
        notas = list(map(float,input(f"Indique as notas das {p} provas do aluno {i+1}: ").split()))

        for k in range(len(notas)):
            somanotas += notas[k]
            if (notas[k] > maiornota10) and notas[k] >= 7:
                maiornota10 = notas[k]
            elif (notas[k] > maiornota7) and 7 > notas[k] >= 4:
                maiornota7 = notas[k]
            
        media = somanotas/(len(notas))

        if (7 > media >= 4) and (media < maiornota7):
            media = maiornota7
        elif media >= 7 and (media < maiornota10):
            media = maiornota10

        medias.append(media)

    for o in range(n):
        print(f"Média do aluno {o+1}: {medias[o]: 0.2f}")
