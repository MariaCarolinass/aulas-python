conversao = int(input("1 - Converter de Celsius para Fahrenheit\n2 - Converter de Fahrenheit para Celsius\nDigite uma opção: "))
temp = int(input("Qual a temperatura: "))

if conversao == 1:
	print(9 / 5 * temp + 32)
elif conversao == 2:
	print(5 / 9 * (temp - 32))
