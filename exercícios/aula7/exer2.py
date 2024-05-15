palindromo = ["ana", "pelo", "ovo", "reviver", "a grama é amarga", "a mala nada na lama",
"telhado", "abacate", "radar", "osso", "viver para viver", "reler", "ame o poema", "sol" , "rever", "sala"]

contar_palindromo = 0
for palavra in palindromo:
    palavra_sem_espacos = palavra.replace(" ", "")
    if palavra_sem_espacos == palavra_sem_espacos[::-1]:
        print(f"{palavra} é um palíndromo")
        contar_palindromo +=1
    else:
        print(f"{palavra} não é um palíndromo")
