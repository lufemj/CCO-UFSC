def imprevisto (a,b,c,d):
    if (a + 1) <= (b-c-d):
        print("Igor feliz!")
    elif c > (d/2):
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")

alunos, comput, queimados, nocomp = map(int,input("Informe o número de alunos, computadores, computadores queimados por Caio e computadores sem compilador: ").split())

imprevisto (alunos, comput, queimados, nocomp)

