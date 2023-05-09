nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite o seu salário fixo: "))
vendas = float(input("Digite o valor total de vendas no mês: "))

salario_bonus = salario + vendas*0.15


print(f"O salário com bônus de {nome} é R${salario_bonus: 0.2f}.")