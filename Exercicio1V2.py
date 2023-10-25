#IMC 2 codígo
nome = str(input("Insira o seu nome: "))
idade = str(input("Insira a sua idade: "))
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira o seu altura: "))
imc = peso/(altura**2)
imc = round(imc)
if imc < 18.5:
    clas = "Abaixo do peso"
elif 18.5 <= imc < 25:
    clas = "Peso ideal"
elif 25 <= imc < 30:
    clas = "Sobrepeso"
elif 30 <= imc < 35:
   clas = "Obesidade Grau 1"
elif 35 <= imc < 40:
    clas = "Obesidade Grau 2"
else:
    clas = "Obesidade extrema"
print('------------------------------------------------------------------------------')
print("Olá {} você tem {} anos, pesa {} kg".format(nome,idade,peso)) 
print("Possui o imc de {} e a sua classificação é {}".format(imc,clas))
print('------------------------------------------------------------------------------')