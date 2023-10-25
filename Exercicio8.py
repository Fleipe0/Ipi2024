#Descobrir de 5 valores qual é par 
c = 0
for i in range (5):
    n = float(input("Digite um número: "))
    if n % 2 == 0:
        print("O número é par")
        c +=1
    else:
        print("O número é ímpar")      
print("Total de valores pares:",c)