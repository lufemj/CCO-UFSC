def duracao (x, y): 
    if y <= x:
        th = -x + 24 + y
    else:
        th = y - x
    
    print(f"O jogo durou {th} horas.")

ti = int(input("Digite a hora de início do jogo: "))
tf = int(input("Digite a hora do final do jogo: "))

duracao(ti, tf)