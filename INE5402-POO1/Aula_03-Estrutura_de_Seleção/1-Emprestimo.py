ValorI = float(input('Valor do Imóvel: '))
SalarioC = float(input('Salário mensal: '))
Periodo = (float(input('Em quantos anos será quitado? ')))*12
Prestacao = ValorI/Periodo

if Prestacao <= SalarioC*0.3:
    print(f"Empréstimo Concedido, o valor da prestação será R${Prestacao: .2f} mensais")
else:
    print("Empréstimo Negado")