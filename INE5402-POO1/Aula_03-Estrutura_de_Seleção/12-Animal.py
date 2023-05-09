c1 = input("Dê a característica 1: ")
c2 = input("Dê a característica 2: ")
c3 = input("Dê a característica 3: ")

if c1 == "vertebrado":
    if c2 == "ave":
        if c3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if c3 == "herbivoro":
            print("vaca")
        else: 
            print("homem")
else:
    if c2 == "inseto":
        if c3 == "herbivoro":
            print("lagarta")
        else:
            print("pulga")
    else:
        if c3 == "hematogafo":
            print("sanguessuga")
        else:
            print("minhoca")