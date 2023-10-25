#Bhaskara codígo	
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Impossível realizar a operação")
else:
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    x1 = round(x1)
    x2 = round(x2)
    print ("As raízes são ", x1, "e", x2)
