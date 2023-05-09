funcionario = int(input("Digite o número do funcionário: "))
horas = int(input("Digite o número de horas trabalhadas: "))
valor = float(input("Digite o valor que recebe por hora: "))

salario = horas * valor

print(f"O funcionário número {funcionario} recebe R${salario}.")
