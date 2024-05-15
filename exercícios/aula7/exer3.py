frutas = "banana uva maçã melão abacaxi".upper()
frutasList = frutas.split(" ")

if "UVA" in frutas:
    indice = frutasList.index("UVA")
    frutasList[indice] = "MORANGO"

print(frutasList)