def aumento (x):
    if x <= 400:
        reajuste = 15
        salariof = salario * 1.15
    elif x <= 800:
        reajuste = 12
        salariof = salario * 1.12
    elif x <= 1200:
        reajuste = 10
        salariof = salario * 1.10
    elif x <= 2000:
        reajuste = 7
        salariof = salario * 1.07
    else:
        reajuste = 4
        salariof = salario * 1.04
    print(f"O novo salário com {reajuste}% de ajuste é de R${salariof: 0.2f}, o aumento foi de R${(salariof - salario): 0.2f}.")
    
salario = round (float(input("Digite o salário do funcionário: ")), 2)

aumento (salario)
