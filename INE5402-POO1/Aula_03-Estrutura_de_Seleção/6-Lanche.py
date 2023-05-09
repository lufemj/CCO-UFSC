cq = 4.00
xs = 4.50
xb = 5.00
ts = 2.00
ref = 1.50

cod = int(input("Digite o código do lanche: "))
quant = int(input("Digite a quantidade: "))

if cod == 1:
    print(f"Valor total: R${cq*quant: 0.2f}")
elif cod == 2:
    print(f"Valor total: R${xs*quant: 0.2f}")
elif cod == 3:
    print(f"Valor total: R${xb*quant: 0.2f}")
elif cod == 4:
    print(f"Valor total: R${ts*quant: 0.2f}")
else:
    print(f"Valor total: R${ref*quant: 0.2f}")