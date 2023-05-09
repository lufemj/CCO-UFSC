import math

fugitivo = True

while fugitivo:
    d = int(input("Distância das embarcações: "))
    vf = int(input("Velocidade do barco do fugitivo: "))
    vg = int(input("Velocidade do barco do guarda: "))

    h = math.sqrt(d**2 + 12**2)

    if (vg / h) < (vf / 12):
        print("O fugitivo não foi capturado, informe outras condições")
    else:
        fugitivo = False

print("O fugitivo foi capturado com sucesso!")