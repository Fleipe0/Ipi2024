#Descobrir de 5 valores qual é negativo
c = 0
for i in range (5):
    n = float(input("Digite um número: "))
    if n < 0:
        print("O número é negativo")
        c +=1
    else:
        print("O número é positivo")
print("Total de valores negativos:",c)