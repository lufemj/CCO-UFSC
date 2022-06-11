x = True
while x:
    num = int(input("Número de casos: "))
    if 1 <= num <= 1000:
        break
    else:
        print("Número invalido, digite novamente.")
        
l0 = l6 = l9 = 6
l1 = 2
l2 = l3 = l5 = 5
l4 = 4
l7 = 3
l8 = 7

z = 1
leds = 0

while num != 0:
    nled = int(input("Número que deseja ser transformado em LED: "))
    while nled != 0:
        numled = (nled%10)
        if numled == 0 or numled ==  6 or numled ==  9:
            leds += 6
        elif numled == 1:
            leds += 2
        elif numled == 2 or numled ==  3 or numled ==  5:
            leds += 5
        elif numled == 4:
            leds += 4
        elif numled == 7:
            leds += 3
        elif numled == 8:
            leds += 7
        nled = nled // 10
    print(f"{leds} leds")
    leds = 0
    num -= 1