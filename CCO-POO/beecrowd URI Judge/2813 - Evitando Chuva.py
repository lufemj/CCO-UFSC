x = True
while x:
    num = int(input("Número de previstos pelo sistema meteorológico: "))
    if 1 <= num <= 1000:
        break
    else:
        print("Número invalido, digite novamente.")
        
umbr_casa = 0
umbr_trabalho = 0
n = num

while num != 0:
    casa, trabalho = input("Previsão do tempo para casa e para escritório: ").split()
    casa = casa.lower()
    trabalho = trabalho.lower()
    
    if casa == "chuva" and trabalho == "sol":
        umbr_casa += 1
    elif casa ==  "sol" and trabalho == "chuva":
        umbr_trabalho +=  1
    
    if num < n and casa == "chuva" and umbr_trabalho >= 1:
        umbr_casa -= 1
    elif num < n and trabalho == "chuva" and umbr_casa >= 1:
        umbr_trabalho -= 1
    num -= 1
        
        
print (umbr_casa, umbr_trabalho)