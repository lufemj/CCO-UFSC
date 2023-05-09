def fuso (s,t,f):
    horaf = s + t + f
    if horaf > 24:
        horaf -= 24
    elif horaf < 0:
        horaf += 24
    print(f"A hora da chegada da viagem é {horaf}H.")

x = True
while x:
    s, t, f = input("Digite a hora da saída, o tempo de viagem e o fuso horário do destino: ").split()
    s = int(s)
    t = int(t)
    f = int(f)

    if (0 <= s <= 23) and (1 <= t <= 12) and (-5 <= f <= 5):
        break
    else:
        print("Erro nos valores. Digite Novamente.")

fuso (s,t,f)
