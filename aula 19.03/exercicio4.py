palavras = input("Digite palavras separadas por espaço: ").split()
busca = input("Digite a palavra a buscar: ")

for i, palavra in enumerate(palavras):
    if palavra == busca:
        print(f"Encontrada no índice {i}")
        break
else:
    print("Palavra nao encontrada")