soma = 0
int1 = int(input("Primeiro número inteiro: "))
int2 = int(input("Segundo número inteiro: "))

for s in range(int1,int2+1):
    print(s)
    soma=soma+s
print(f"A soma dos números do intervalo é: {soma}")