#Tabuada codígo
n = int(input("Digite um número para ver a tabuada: "))
l = int(input("Digite o limite da tabuada:"))
for c in range (1,l+1):
    print("{} x {} = {}".format(n,c,n*c))

