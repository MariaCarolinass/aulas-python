import math as m

def calcularSen(num):
	sin = m.sin(num)
	return round(m.degrees(sin), 2)

def calcularCos(num):
	cos = m.cos(num)
	return round(m.degrees(cos), 2)
 
def calcularTg(num):
	tg = m.tan(num)
	return round(m.degrees(tg), 2)

sin = calcularSen(45)
cos = calcularCos(45)
tg = calcularTg(45)

max = max(sin, cos, tg)
min = min(sin, cos, tg)

print(f"Seno: {sin}")
print(f"Cosseno: {cos}")
print(f"Tangente: {tg}")

print(f"Valor máximo: {max}")
print(f"Valor minimo: {min}")