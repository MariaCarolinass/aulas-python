pessoas = []

for i in range(1, 6):
	nome = str(input("Nome: "))
	idade = int(input("Idade: "))
	estadocivil = str(input("Estado civil: "))
	pessoa = [nome, idade, estadocivil]
	pessoas.append(pessoa)

print(pessoas)
