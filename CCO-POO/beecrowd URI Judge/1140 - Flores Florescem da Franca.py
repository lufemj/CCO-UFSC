while True:
    taut = []
    tautologia = "Y"
    frase = input().split()
    if frase == ["*"]:
        break
    else:
        for i in range(len(frase)):
            letra = frase[i][0].upper()
            taut.append(letra)

        for j in range (len(taut)):
            if tautologia == "N":
                break
            else:
                if taut[0] == taut[j]:
                    tautologia = "Y"
                else:
                    tautologia = "N"
                    break

    print(tautologia)

    #LufeMJ
            