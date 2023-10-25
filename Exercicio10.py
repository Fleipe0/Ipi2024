#Fatorial código
n = int(input("Digite um número para ver o fatorial:"))
cont = 0 
f = 1
for cont in  (f,n+1):
    f = f * cont
    cont = cont + 1
print("O Fatorial de {} é {}".format(n,f))