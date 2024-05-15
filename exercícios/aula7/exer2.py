palindromo = ["ana", "pelo", "ovo", "reviver",
"telhado", "abacate", "radar", "osso", "reler", "sol" , "rever", "sala"]

contar_palindromo = 0
for palavra in palindromo:
    if palavra == palavra[::-1]:
        print(f"{palavra} é um palíndromo")
        contar_palindromo +=1
    else:
        print(f"{palavra} não é um palíndromo")