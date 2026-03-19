a = int(input("Digite a: "))
b = int(input("Digite b: "))
p = int(input("Digite p: "))

if p == 0:
    print("Erro: passo não pode ser 0")
else:
    if a < b and p < 0:
        print("Erro: passo deve ser positivo")
    elif a > b and p > 0:
        print("Erro: passo deve ser negativo")
    else:
        contador = 0

        # Ajuste para incluir b
        if (p > 0 and a <= b) or (p < 0 and a >= b):
            for i in range(a, b + (1 if p > 0 else -1), p):
                print(i, end=" ")
                contador += 1

        print(f"\nQuantidade de valores: {contador}")