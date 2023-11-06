#Imc 1 código
nome = str(input("Insira o seu nome: "))
idade = str(input("Insira a sua idade: "))
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira o seu altura: "))
imc = peso/(altura*altura)
imc = round(imc)
print("Olá {} você tem {} anos e pesa {} kg e possui o imc de {}".format(nome,idade,peso,imc))