x = True
while x:
    num = int(input("Número de casos do jogo: "))
    if 1 <= num <= 1000:
        break
    else:
        print("Número invalido, digite novamente.")
       

while num != 0:
    jogo = input("Dê a sequência do jogo: ")
    if int(jogo[:1]) or int(jogo[2:3]):
        x = 2
    else:
        print("Erro")
    num1 = int(jogo[:1])
    num2 = int(jogo[2:3])
    letra = jogo[1:2]
    if num1 == num2:
        print(num1 * num2)
    elif letra == letra.upper():
        print(num2 - num1)
    else:
        print(num1 + num2)
    num -= 1
        
    
    