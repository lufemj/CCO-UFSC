s=0
n=int(input("Digite um número inteiro: "))
for i in range(n,1):
    bx=n%i
    if bx==0:
        s=s+1
if s==2 :
    print("O número digitado é primo.")
else :
    print("O número digitado não é primo") 