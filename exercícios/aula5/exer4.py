notaPython = int(input("Digite uma avaliação de 0-5 para Python: "))
notaJS = int(input("Digite uma avaliação de 0-5 para JavaScript: "))
notaC = int(input("Digite uma avaliação de 0-5 para C++: "))
notaJava = int(input("Digite uma avaliação de 0-5 para Java: "))
notaPHP = int(input("Digite uma avaliação de 0-5 para PHP: "))

linguagens = {"Python": notaPython, "JavaScript": notaJS, "C++": notaC, "Java": notaJava, "PHP": notaPHP}

print("Ranking das Linguagens")
#for linguagem in sorted(linguagens, key = linguagens.get):
#	print(f"{linguagem}: {linguagens[linguagem]}")

linguagensRanking = {}
for avaliacao in sorted(linguagens.values()):
	for linguagem, avali in linguagens.items():
		if avali == avaliacao:
			linguagensRanking[linguagem] = avali
			break

print(linguagensRanking)
