def dados (x):
    media = 0
    somaidades = 0
    mulhersalario = 0
    menorsalario = 9999999999999
    idadesalario = 0
    maioridade = 0
    maisvelho = 0
    sexosalario = 0
    
    for i in range (1, x+1):
        nome, idade, sexo, salario = input(f"Informe os seguintes dados do {i}° entrevistado separados por espaço: Nome Idade Sexo[M/F] Salário // ").split()
        idade = int(idade)
        salario = float(salario)
        sexo = sexo.upper()
        somaidades += idade

        if i == (x):
            media = somaidades/x

        if sexo == "F" and salario > 2000:
            mulhersalario += 1
        
        if salario < menorsalario:
            menorsalario = salario
            idadesalario = idade
            sexosalario = sexo

        if idade > maioridade:
            maisvelho = nome 
            maioridade = idade   

    print(f"A média de idades do grupo dos entrevistados é: {media:0.1f} anos.")
    print(f"Existem {mulhersalario} mulhere(s) entrevistadas com salário menor que R$2000,00.")
    print(f"A pessoa com menor salário é {sexosalario} e tem {idadesalario} anos.")
    print(f"O morador mais velho é {maisvelho}")

exec = "S"
while exec == "S":
    entrevistados = int(input("Quantos moradores foram entrevistados? "))
    
    dados(entrevistados)


    exec = input("Deseja continuar executando? [S/N] ")
    exec = exec.upper()

