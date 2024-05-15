pessoasList = []

for i in range(1, 3):
	nome = str(input("Nome: "))
	idade = int(input("Idade: "))
	estadocivil = str(input("Estado civil: "))
	pessoa = [nome, idade, estadocivil]
	pessoasList.append(pessoa)

pessoa_mais_velha = ""
mais_velho = 0
solteiro = 0
casado = 0

for pessoas in pessoasList:
	if mais_velho < pessoas[1]:
		mais_velho = pessoas[1]
		pessoa_mais_velha = pessoas[0]
	if pessoas[2] == "solteiro" or pessoas[2] == "solteira":
		solteiro += 1
	if pessoas[2] == "casado" or pessoas[2] == "casada":
		casado += 1

print(pessoasList)
print(f"O mais velho da lista é {pessoa_mais_velha} com {mais_velho} anos")
print(f"Temos {solteiro} pessoas solteiras e {casado} pessoas casadas na lista")
