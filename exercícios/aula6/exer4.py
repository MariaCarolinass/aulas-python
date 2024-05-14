num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = lambda n1, n2: n1 + n2
sub = lambda n1, n2: n1 - n2
multi = lambda n1, n2: n1 * n2
divi = lambda n1, n2: n1 / n2

print(soma(num1, num2))
print(sub(num1, num2))
print(multi(num1, num2))
print(divi(num1, num2))
