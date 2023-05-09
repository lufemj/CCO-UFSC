np = int(input("Quantas praias deseja cadastrar? "))
x = 1
nd = 0
praia_mlonge = 0
distancia_mlonge = 0
total_dist = 0

while x <= np:
    nome_praia = input(f"Nome da praia {x}: ")
    distancia = int(input("Distância que ela está da cidade: "))

    if distancia > distancia_mlonge:
        praia_mlonge = nome_praia
        distancia_mlonge = distancia
    
    if 15 <= distancia <= 20:
        nd += 1
    
    total_dist += distancia
    x += 1

media = total_dist / np

print(f"A praia mais longe é: {praia_mlonge}, a {distancia_mlonge}km de distância.")
print(f"Exitem {nd} praias entre 15km e 20km de distância.")
print(f"A distância média das praias é de {media: 0.1f}km.")
