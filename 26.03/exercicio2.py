from collections import Counter

def filtrar_frequencia(lista, minimo=3):
    contagem = Counter(lista)
    return [num for num, freq in contagem.items() if freq >= minimo]

# Resultado
lista = [1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
print(filtrar_frequencia(lista, 3))
