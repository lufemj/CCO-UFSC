previdencia = True
desconto = 0
salario = 0

while previdencia:
    salario = float(input("Informe o seu salário: "))
    desconto = salario * 0.11
    if desconto > 320:
        desconto = 320
        descontado = 320 / salario
        print(f"Seu salário com {descontado: 0.2f}% de desconto será {salario - 320}")
    else:
        print(f"Seu salário com desconto de R${desconto} será R${salario - desconto}")
    p = input("Deseja continuar? S / N ")
    if p != "S":
        previdencia = False
