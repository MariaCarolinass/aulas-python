nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do aluno é {media}")

aprovacao = False

if media >= 6:
	aprovacao = True

print(f"O resultado do aluno para aprovado é: {aprovacao}")
