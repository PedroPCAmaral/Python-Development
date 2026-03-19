n = int(input("Digite um número inteiro maior que 0: "))

soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

print("Soma dos divisores:", soma)

if soma == n:
    print("Classificação: perfeito")
elif soma > n:
    print("Classificação: abundante")
else:
    print("Classificação: deficiente")
