#Álcool e Gasolina código
alc = float(input("Digite o valor do álcool: "))
gsl = float(input("Digite o valor da gasolina: "))
rs = (alc/gsl)*100
rs = round(rs)
print("A relação de preços é de",rs,"%")
print('----------------------------------')
if rs >= 70:
    print("A gasolina é mais vantajosa")
else:
     print("O álcool é mais vantajoso") 
print('----------------------------------')