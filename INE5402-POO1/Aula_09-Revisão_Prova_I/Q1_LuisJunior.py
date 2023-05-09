exec = "S"

while exec == "S":
    a, p, c, m, i = input("Dê as porções de todos: [Inteiros, separados por espaço] ").split()

    #Andre
    a = int(a)
    #Pedro
    p = int(p)
    #Camila
    c = int(c)
    #Manoel
    m = int(m)
    #Iara
    i = int(i)

    gramastotal = (a*300)+(p*1500)+(c*600)+(m*1000)+(i*150)+225

    print(gramastotal)

    exec = input("Deseja continuar executando? [S/N] ")
    exec = exec.upper()

