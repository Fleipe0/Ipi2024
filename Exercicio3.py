#Viagem codígo
gas = float(input("Digite o valor da gasolina: "))
km = float(input("Digite a distância: "))
cons = float(input("Digite o consumo do carro: "))
rs = (km/cons)*gas
rs = round(rs)
print("O valor da viagem vai ser R$",rs)
