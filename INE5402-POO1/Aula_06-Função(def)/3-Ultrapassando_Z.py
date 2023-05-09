def ultrapassar (x,z):
    a = 2
    n = x
    for i in range (x, z+1):
        n += i
        if n > z:
            print (a)
            break
        else: 
            a +=1
        
x,z = input("Digite dois valores inteiros para X e Z: ").split()
x = int(x)
z = int(z)

while z <= x:
    print("Z é menor que X.")
    z = int(input("Digite um novo valor para Z: "))

ultrapassar (x,z)
