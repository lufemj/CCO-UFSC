def imprevisto (a,b,c,d):
    if (a + 1) <= (b-c-d):
        print("Igor feliz!")
    elif c > (d/2):
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")


alunos = int(input("Número de alunos: "))
comput = int(input("Número de computadores: "))
queimados = int(input("Número de computadores queimados por Caio: "))
nocomp = int(input("Número de computadores sem compilador: "))

imprevisto (alunos, comput, queimados, nocomp)

