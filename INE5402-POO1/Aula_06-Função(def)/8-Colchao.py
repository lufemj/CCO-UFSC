def passagem (a, b, h, l):
    passar = "S"
    if a > l:
        passar = "N"
    elif b > h:
        passar = "N"

    return passar

while True:
    a, b, c = map(int,input("Indique as dimensões do colchão em centímetros: ").split())

    if 1 <= a <= 300 and 1 <= b <= 300 and 1 <= c <= 300:
        break
    else:
        print("Dados do colchão invalidos, digite novamente.")


while True:
    h, l = map(int,input("Indique as dimensões das portas em centímetros: ").split())

    if 1 <= h <= 250 and 1 <= l <= 250:
        break
    else:
        print("Dados das portas invalidos, digite novamente.")

    
passou = passagem(a, b, h, l)

if passou == "S":
    print("Parabéns, o colchão é do tamanho adequado!")
elif passou == "N":
    print("Infelizmente você deve procurar outro colchão.")