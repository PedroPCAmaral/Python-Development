def normalizar(texto):
    return sorted(
        c.lower() for c in texto if c.isalnum()
    )

def sao_anagramas(t1, t2):
    return normalizar(t1) == normalizar(t2)


# Exemplo.
frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")

if sao_anagramas(frase1, frase2):
    print("São anagramas!")
else:
    print("Não são anagramas.")