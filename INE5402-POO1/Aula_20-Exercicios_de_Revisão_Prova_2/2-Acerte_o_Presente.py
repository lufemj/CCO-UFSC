while True:
    x = int(input("Informe a quantidade de participantes do amigo secreto: "))
    if 3 <= x <= 20:
        break
    else:
        print("Erro. Digite novamente.")

dic = {}
        
for i in range(x):
    pessoa, sugest1, sugest2, sugest3 = input(f"Informe o nome da pessoa {i+1} e os presentes que ela deseja: ").split()
    dic[pessoa] = [sugest1, sugest2, sugest3]

while True:
    nome, presente = input(f"Informe o nome da pessoa e o presente que ela vai receber: ").split()
    if presente in dic[nome]:
        print("Uhul! Seu amigo secreto vai adorar o/")
    else:
        print("Tente Novamente!")

    cont = input("Deseja continuar?  S/N ")
    if cont.upper() != "S":
        break

