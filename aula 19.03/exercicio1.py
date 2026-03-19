import string

def eh_palindromo(texto):
    # Remove espaços, pontuações e normaliza para minúsculas
    texto_limpo = ''.join(
        c.lower() for c in texto if c.isalnum()
    )
    return texto_limpo == texto_limpo[::-1]

# Exemplo
frase = input("Digite uma frase: ")
if eh_palindromo(frase):
    print("É palíndromo!")
else:
    print("Não é palíndromo.")  