nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 4:
	print("Reprovado por média")
elif media >= 4 and media < 6:
	print("Em recuperação")
elif media >= 6 and media <= 10:
	print("Aprovado por média")
