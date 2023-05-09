s=0
NUMERO=int(input("Digite um número inteiro: "))
for i in range(1,(NUMERO+1)):
    bx=NUMERO%i
    if bx==0:
        s=s+1
        print(f"O número é divisivel por {i}")
if s==2 :
    print("O número digitado é primo.")
else :
    print("O número digitado não é primo")