jogo = 1

while jogo <= 15:
    m = int(input(f"Dê os pontos da primeira equipe do jogo {jogo}: "))
    n = int(input(f"Dê os pontos da segunda equipe do jogo {jogo}: "))

    if jogo == 1:
        if m > n:
            qf9_1 = "A"
        else:
            qf9_1 = "B"
    elif jogo == 2:
        if m > n:
            qf9_2 = "C"
        else:
            qf9_2 = "D"
    elif jogo == 3:
        if m > n:
            qf10_1 = "E"
        else:
            qf10_1 = "F"
    elif jogo == 4:
        if m > n:
            qf10_2 = "G"
        else:
            qf10_2 = "H"
    elif jogo == 5:
        if m > n:
            qf11_1 = "I"
        else:
            qf11_1 = "J"
    elif jogo == 6:
        if m > n:
            qf11_2 = "K"
        else:
            qf11_2 = "L"
    elif jogo == 7:
        if m > n:
            qf12_1 = "M"
        else:
            qf12_1 = "N"
    elif jogo == 8:
        if m > n:
            qf12_2 = "O"
        else:
            qf12_2 = "P"
    elif jogo == 9:
        if m > n:
            sf13_1 = qf9_1
        else:
            sf13_1 = qf9_2
    elif jogo == 10:
        if m > n:
            sf13_2 = qf10_1
        else:
            sf13_2 = qf10_2
    elif jogo == 11:
        if m > n:
            sf14_1 = qf11_1
        else:
            sf14_1 = qf11_2
    elif jogo == 12:
        if m > n:
            sf14_2 = qf12_1
        else:
            sf14_2 = qf12_2
    elif jogo == 13:
        if m > n:
            f15_1 = sf13_1
        else:
            f15_1 = sf13_2
    elif jogo == 14:
        if m > n:
            f15_2 = sf14_1
        else:
            f15_2 = sf14_2
    elif jogo == 15:
        if m > n:
            vencedor = f15_1
        else:
            vencedor = f15_2

    jogo += 1

print (f"O time vencedor foi o time {vencedor}")
