a = int(input("Qual o valor de a: "))
b = int(input("Qual o valor de b: "))
c = int(input("Qual o valor de c: "))

delta = b ** 2 - 4 * a * c
x1 = (- b + delta ** (1/2)) / (2 * a)
x2 = (- b - delta ** (1/2)) / (2 * a)

print(delta)
print(x1)
print(x2)
