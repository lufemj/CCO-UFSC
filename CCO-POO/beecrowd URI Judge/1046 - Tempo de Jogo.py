def duracao (x, y): 
    if y <= x:
        th = -x + 24 + y
    else:
        th = y - x
    
    print(f"O jogo durou {th} hora(s).")

ti, tf = map(int,input("Digite a hora de início e final do jogo: ").split())

duracao(ti, tf)