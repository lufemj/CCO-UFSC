while True:    
    n = int(input("Informe o numero de casos teste: "))
    if n == 0:
        break

    alunos = []
    assinaturas = []
    falsos = 0

    for i in range (n):
        nome, assori = input("Informe o nome do aluno e sua assinatura original: ").split()
        alunos.append(nome)
        assinaturas.append(assori)

    m = int(input("Informe o numero de alunos presentes: "))

    for j in range(m):
        erros = 0
        n, assaula = input("Informe o nome do aluno e sua assinatura na aula: ").split()
        k = alunos.index(n)
        for o in range(len(alunos[k])):
            if assinaturas[k][o] != assaula[o]:
                erros += 1
            if erros > 1:
                falsos += 1
                break
    print (falsos)