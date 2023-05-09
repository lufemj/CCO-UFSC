n = int(input("Quantos depósitos foram feitos no cofrinho? "))
resto = 0

while n != 0:
    j = int(input("Qual moeda foi colocada no cofrinho de Joãozinho? "))
    z = int(input("Qual moeda foi colocada no cofrinho de Zézinho? "))
    dif = j - z + resto
    if dif > 0:
        print(f"Joãozinho tem {dif} de moedas a mais.")
        resto = dif
    elif dif < 0:
        print(f"Zézinho tem {-dif} de moedas a mais.")
        resto = dif
    else:
        print("O dois cofrinhos tem os mesmos valores")
        resto = dif
    n -= 1