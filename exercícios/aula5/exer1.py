nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a nota do aluno: "))
nota3 = float(input("Digite a nota do aluno: "))

notas = [nota1, nota2, nota3]

maior_nota = 0
media = 0

for nota in notas:
	media += nota	
	if nota > maior_nota:
		maior_nota = nota

media /= 3

print(f"A maior nota da lista é {maior_nota}")
print(f"A média das notas é {media}")
