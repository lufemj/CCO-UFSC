def combustivel (x, y):
    combustivel = (x * y) / 12

    print(f"A quantidade de combustível necessária é de {combustivel: 0.3f}L.")


tempov = int(input("Dê o tempo da viagem em horas: "))
velocidadem = int(input("Dê a velocidade média em km/h: "))

combustivel (tempov, velocidadem)