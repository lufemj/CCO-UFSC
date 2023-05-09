idade_dias = int(input("Digite a sua idade em dias: "))

idade_ano = idade_dias // 365
resto_mes = idade_dias % 365
idade_mes = resto_mes // 30
idade_dias = resto_mes % 30


print(f"Sua idade é {idade_ano} anos, {idade_mes} meses e {idade_dias} dias.")