altura = float(input("Digite a sua altura: "))
peso = int(input("Digite o seu peso: "))

imc = peso / (altura * altura)

print(f"O seu IMC é: {round(imc, 2)}")
