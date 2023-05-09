# 1.Álcool 2.Gasolina 3.Diesel 4.Fim

n = 0
alcool = 0
gasolina = 0
diesel = 0

while n != 4:
    n = int(input("Digite qual dos produtos é de sua preferencia? "))
    if 1 <= n <= 3:   
        if n == 1:
            alcool += 1
        elif n == 2:
            gasolina += 1
        else:
            diesel += 1    
    else:
        print("O número informado é invalido.")

print("Muito Obrigado")
print(f"Álcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
