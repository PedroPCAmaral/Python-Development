def crivo():
    tamanho = 1000

    # a) cria o array com tudo = 1
    vetor = [1] * tamanho

    # ignora 0 e 1
    vetor[0] = 0
    vetor[1] = 0

    # b) começa do índice 2
    for i in range(2, tamanho):
        if vetor[i] == 1:  # se ainda é primo
            # marca os múltiplos como 0
            for j in range(i * 2, tamanho, i):
                vetor[j] = 0

    # imprime os primos
    for i in range(2, tamanho):
        if vetor[i] == 1:
            print(i, end=" ")

# Executa
crivo()
