rs = float(input("Valor monetário: "))
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0 
cent_50 = 0
cent_25 = 0
cent_10 = 0
cent_5 = 0
cent_1 = 0

while rs != 0:
   if (rs - 100) >= 0:
      rs -= 100
      cem += 1
   elif (rs - 50) >= 0:
      rs -= 50
      cinquenta += 1
   elif (rs - 20) >= 0:
      rs -= 20
      vinte += 1
   elif (rs - 10) >= 0:
      rs -= 10
      dez += 1
   elif (rs - 5) >= 0:
      rs -= 5
      cinco += 1
   elif (rs - 2) >= 0:
      rs -= 2
      dois += 1
   elif (rs - 1) >= 0:
      rs -= 1
      um += 1
   elif (rs - 0.5) >= 0:
      rs -= 0.5
      cent_50 += 1
   elif (rs - 0.25) >= 0:
      rs -= 0.25
      cent_25 += 1
   elif (rs - 0.1) >= 0:
      rs -= 0.1
      cent_10 += 1
   elif (rs - 0.05) >= 0:
      rs -= 0.05
      cent_5 += 1
   elif (rs - 0.01) >= 0:
      rs -= 0.01
      cent_1 += 1
   else: 
      break
   
print("Notas:")
print(cem,"nota(s) de R$ 100")
print(cinquenta,"nota(s) de R$ 50")
print(vinte,"nota(s) de R$ 20")
print(dez,"nota(s) de R$ 10")
print(cinco,"nota(s) de R$ 5")
print(dois,"nota(s) de R$ 2")
print("Moedas:")
print(um,"moeda(s) de R$ 1")
print(cent_50,"moeda(s) de R$ 0,50")
print(cent_25,"moeda(s) de R$ 0,25")
print(cent_10,"moeda(s) de R$ 0,10")
print(cent_5,"moeda(s) de R$ 0,05")
print(cent_1,"moeda(s) de R$ 0,01")