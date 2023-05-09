from random import randrange

random = randrange(11)
tent = 1
num = int(input("Qual seu número: "))
    

while num != random:
    print("Errado.")
    num = int(input("Tente Novamente: "))
    tent += 1

print(f"Parabéns, você acertou o número secreto {random} após {tent} tentativas!")