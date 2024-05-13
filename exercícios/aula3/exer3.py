idade = int(input("Qual a sua idade: "))
carteira = str(input("Tem carteira de motorista (sim/não)? "))

if idade >= 18 and carteira == "sim":
	print("Hábitado para dirigir")
else:
	print("Não hábito para dirigir")
