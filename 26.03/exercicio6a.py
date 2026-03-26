def crivo_eratostenes(n):
    primos = [1] * (n + 1)
    primos[0] = primos[1] = 0

    for i in range(2, n + 1):
        if primos[i] == 1:
            for j in range(i * 2, n + 1, i):
                primos[j] = 0

    return [i for i in range(2, n + 1) if primos[i] == 1]

# Testando
print(crivo_eratostenes(999))
