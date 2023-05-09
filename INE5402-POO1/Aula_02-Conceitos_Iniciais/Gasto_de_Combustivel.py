tempov = int(input("Dê o tempo da viagem em horas: "))
velocidadem = int(input("Dê a velocidade média em km/h: "))


combustivel = (tempov * velocidadem) / 12

print(f"A quantidade de combustível necessária é de {combustivel: 0.3f}L.")