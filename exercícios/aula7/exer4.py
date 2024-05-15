nome_completo = str(input("Digite seu nome completo: "))

if "de" in nome_completo:
    nome_completo = nome_completo.replace(" de ", " ")

tamanho_nome = len(nome_completo)

dividir_nome = nome_completo.split(" ")
primeiro_nome = dividir_nome[0]
último_nome = dividir_nome[len(dividir_nome)-1]

nome = primeiro_nome + " " + último_nome

print(nome_completo)
print(tamanho_nome, "caracteres")
print(nome)
