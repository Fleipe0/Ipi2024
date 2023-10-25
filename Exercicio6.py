#Media e classificação da nota codígo
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

media = (n1+n2+n3)/3
media = round(media)

if media < 59:
    print("Conceito C, pois a média é", media)
elif 59 <= media < 79:
    print("Conceito B, pois a média é", media)
else:
    print("Conceito A,pois a média é", media)
