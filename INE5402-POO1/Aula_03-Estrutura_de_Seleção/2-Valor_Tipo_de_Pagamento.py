ValorP = float(input('Valor do Produto: '))
MeioP = input('Pagamento à vista(Dinheiro/Cheque)? SIM / NAO : ')
if MeioP == "SIM":
    print(f"O valor será Rs{ValorP*0.9}")
else:
    parcelas = int(input("Número de parcelas no cartão:"))
    if (parcelas == 1):
        print(f"O valor será Rs{ValorP*0.95}")
    elif (parcelas == 2):
        print(f"O valor será Rs{ValorP}")
    else:
        print(f"O valor será Rs{ValorP*1.20}")