num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

operacao = int(input("Qual operação matemática deseja realizar? \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite um número: "))

if operacao == 1:
	soma = num1 + num2	
	print(soma)
elif operacao == 2:
	sub = num1 - num2
	print(sub)
elif operacao == 3:
	mult = num1 * num2
	print(mult)
elif operacao == 4:
	div = num1 / num2
	print(div)
