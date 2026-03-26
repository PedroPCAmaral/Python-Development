def soma_subconjunto(nums, alvo):
    possiveis = {0}

    for num in nums:
        novas_somas = set()
        for s in possiveis:
            novas_somas.add(s + num)
        possiveis |= novas_somas

    return alvo in possiveis

# Resultado
lista = [3, 34, 4, 12, 5, 2]
alvo = 9
print(soma_subconjunto(lista, alvo)) 
