def verificar_parenteses(expr):
    pilha = []

    for char in expr:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if not pilha:
                return "Erro"
            pilha.pop()

    return "OK" if not pilha else "Erro"

# Resultado
print(verificar_parenteses("(())"))
print(verificar_parenteses("()()(()())"))
print(verificar_parenteses("())"))
