x = True
while x:
    num = int(input("Número de comandos do sargento: "))
    if 1 <= num <= 1000:
        break
    else:
        print("Número invalido, digite novamente.")
       
comando = input("Comando do Sargento: ")
comando = comando.upper()

esq = int(comando.count("E"))
dir = int(comando.count("D"))

if esq > dir:
    virar = esq - dir
    while virar > 4:
        virar -= 4
    if virar == 1:
        direcao = "O"
    elif virar == 2:
        direcao = "S"
    elif virar == 3:
        direcao = "L"
    else:
        direcao = "N"
elif dir > esq:
    virar = dir - esq
    while virar > 4:
        virar -= 4
    if virar == 1:
        direcao = "L"
    elif virar == 2:
        direcao = "S"
    elif virar == 3:
        direcao = "O"
    else:
        direcao = "N"
else: direcao = "N"
        
print(direcao)