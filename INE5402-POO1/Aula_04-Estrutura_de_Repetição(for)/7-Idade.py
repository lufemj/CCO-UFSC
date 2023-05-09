n = int(input("Número de pessoas: "))
media = 0
sidade=0
for P in range(1,n+1):
    idade = int(input(f"Idade da Pessoa n.{P}: "))
    sidade = sidade+idade
media=sidade/n
if media<26:
    print("A turma é jovem!")
elif media<61:
    print("A turma é adulta!")
else:
    print("A turma é idosa!")