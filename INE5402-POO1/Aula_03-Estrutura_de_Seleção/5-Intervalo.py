valor = float(input("Digite o valor: "))


if valor >= 0 and valor <= 25:
    print("Intervalo [0,25]")
elif valor >  25 and valor <= 50:
    print("Intervalo (25,50]")
elif valor > 50 and valor <= 70:
    print("Intervalo (50,70]")
elif valor > 70 and valor <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")