xa = float(input("Qual o valor de x no ponto a? "))
ya = float(input("Qual o valor de y no ponto a? "))

xb = float(input("Qual o valor de x no ponto b? "))
yb = float(input("Qual o valor de y no ponto b? "))

a = (xa, ya)
b = (xb, yb)

dist = ((b[0] - a[0]) ** 2 + (b[1] - a[1])) / (1/2)
print(dist)
