nome_completo = str(input("Digite seu nome completo: "))

if "de" in nome_completo:
    nome_completo = nome_completo.replace(" de ", " ")

tamanho_nome = len(nome_completo)

print(nome_completo)
print(tamanho_nome, "caracteres")