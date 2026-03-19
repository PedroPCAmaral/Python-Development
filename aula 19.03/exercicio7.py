n = int(input("Digite um número inteiro: "))

if n < 0:
    print("Erro: número negativo")
else:
    fatorial = 1

    for k in range(1, n + 1):
        fatorial *= k

        if fatorial > 1000000:
            print(f"Passou do limite em {k}!")
            print("Valor acumulado:", fatorial)
            break
    else:
        print("Fatorial:", fatorial)
