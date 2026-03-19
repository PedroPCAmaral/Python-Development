estado = "fechado"

while True:
    comando = input("Digite comando (A, T, E, F, S): ").upper()

    match comando:
        case "A":
            estado = "aberto"
            print("Atendimento aberto")

        case "T":
            if estado == "aberto":
                estado = "triado"
                print("Triagem realizada")
            else:
                print("Erro: precisa estar aberto")

        case "E":
            if estado == "triado":
                estado = "encaminhado"
                print("Encaminhado")
            else:
                print("Erro: precisa estar triado")

        case "F":
            if estado == "encaminhado":
                estado = "fechado"
                print("Atendimento finalizado")
            else:
                print("Erro: precisa estar encaminhado")

        case "S":
            print("Saindo...")
            break

        case _:
            print("Comando inválido")