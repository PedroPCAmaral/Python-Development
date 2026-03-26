def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    print("Comuns:", set1 & set2)
    print("Só na primeira:", set1 - set2)
    print("Só na segunda:", set2 - set1)
    print("Sem repetição (união):", set1 | set2)
    print("Primeira sem repetidos da segunda:", set1 - set2)
    print("listas todas juntas ")

# Resultado
l1 = [1,2,3,4]
l2 = [3,4,5,6]
comparar_listas(l1, l2)
