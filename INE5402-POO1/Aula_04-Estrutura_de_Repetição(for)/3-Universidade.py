mediap = 0
for i in range(5):
    nome = input("Nome do Aluno: ")
    mediag = float(input(f"Média do Aluno {nome}: "))
    mensalidade = float(input(f"Mensalidade do Aluno {nome}: "))
    if mediag > mediap:
        nomep = nome
        mediap = mediag
        mensalidadep = mensalidade*0.7
print(f"Desconto para {nomep}, com a média: {mediap},o valor da mensalidade será de Rs {mensalidadep: .2f}")
    
    

