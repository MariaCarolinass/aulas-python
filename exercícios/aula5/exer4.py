linguagens = {"Python": 0, "JavaScript": 0, "C++": 0, "Java": 0, "PHP": 0}

for linguagem in linguagens:
	avaliacao = int(input(f"Digite uma avaliação de 0-5 para {linguagem}: "))
	linguagens[linguagem] = avaliacao

melhor_linguagem = ""
pior_linguagem = ""
maior_avaliacao = -1
menor_avaliacao = 6

for linguagem, avaliacao in linguagens.items():
	if avaliacao > maior_avaliacao:
		maior_avaliacao = avaliacao
		melhor_linguagem = linguagem
	if avaliacao < menor_avaliacao:
		menor_avaliacao = avaliacao
		pior_linguagem = linguagem

print(f"{melhor_linguagem} teve a melhor avaliação igual a {maior_avaliacao}")
print(f"{pior_linguagem} teve a pior avaliação igual a {menor_avaliacao}")
