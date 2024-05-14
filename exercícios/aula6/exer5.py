import random

n1 = n2 = n3 = n4 = n5 = n6 = 0

for n in range(0, 10):
	num = random.randint(1, 6)
	print(f"Valor sorteado: {num}")

	if num == 1:
		n1 += 1
	if num == 2:
		n2 += 1
	if num == 3:
		n3 += 1
	if num == 4:
		n4 += 1
	if num == 5:
		n5 += 1
	if num == 6:
		n6 += 1

print(f"O número 1 foi sorteado: {n1} vezes")
print(f"O número 2 foi sorteado: {n2} vezes")
print(f"O número 3 foi sorteado: {n3} vezes")
print(f"O número 4 foi sorteado: {n4} vezes")
print(f"O número 5 foi sorteado: {n5} vezes")
print(f"O número 6 foi sorteado: {n6} vezes")
