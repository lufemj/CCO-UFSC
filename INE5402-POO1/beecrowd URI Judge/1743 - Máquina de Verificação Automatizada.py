x = list(map(int,input("Informe os pontos de conexão do primeiro conector: ").split()))
y = list(map(int,input("Informe os pontos de conexão do segundo conector: ").split()))
x_ = []

for i in x:
    if i == 1:
        x_.append(0)
    else:
        x_.append(1)
if x_ == y:
    print('Y')
else:
    print('N')