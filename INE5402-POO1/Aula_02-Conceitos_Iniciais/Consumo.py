distancia = int(input("Dê o distância percorrida em km: "))
combustivel = float(input("Dê o combustível gasto em L: "))

consumo = distancia / combustivel

print(f"O consumo médio do automóvel é de {consumo: 0.3f} km/L.")