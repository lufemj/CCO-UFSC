dados = []
cadastros = 1
maior_peso = [0, 0, 0]
menor_peso = [0,0, 999]
maior_20 = [0, 0, 0]

while True:
    info = input("Informe respectivamente o nome, a idade e o peso da pessoa: ").split()
    info[1] = int(info[1])
    info[2] = int(info[2])

    dados.append(info)

    seguir = input("Deseja continuar cadastrando?  S/N ")
    seguir = seguir.upper()
    if seguir != "S":
        break

    cadastros += 1

for i in range (len(dados)):
    
#Pessoas com o maior peso
    if i == 0:
            maior_peso = [dados[i]]

    else:
        if dados[i][2] > maior_peso[0][2]:
            maior_peso = [dados[i]]
        elif dados[i][2] == maior_peso[0][2]:
            maior_peso.append(dados[i])

#Pessoas com o menor peso
    if i == 0:
            menor_peso = [dados[i]]

    else:
        if dados[i][2] < menor_peso[0][2]:
            menor_peso = [dados[i]]
        elif dados[i][2] == menor_peso[0][2]:
            menor_peso.append(dados[i])

#Pessoas acima de 20 anos
    if dados[i][1] > 20:
        if maior_20[0] == 0:
            maior_20 = [dados[i][0:2]]
        else:
            maior_20.append(dados[i][0:1])

print(f"O número de pessoas cadastradas foi: {cadastros}.")
print(f"A(s) pessoa(s) mais pesada(s): {maior_peso}.")
print(f"A(s) pessoa(s) mais leve(s): {menor_peso}.")
print(f"O número de pessoas acima de 20 anos foi: {len(maior_20)}, sendo ela(s): {maior_20}.")