peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura**2)

if (imc <= 18.5) :
    print("Você está abaixo do peso.")
elif (imc <= 25) :
    print("Você está no peso ideal.")
elif (imc <= 30) :
    print("Você está com sobrepeso.")
elif (imc <= 40) :
    print("Você tem obesidade.")
else :
    print("Você tem obesidade morbida.")