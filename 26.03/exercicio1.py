def mesclar_intervalos(intervalos):
    intervalos.sort()  #ordena pelo comeco
    resultado = []

    for inicio, fim in intervalos:
        if not resultado or inicio > resultado[-1][1]:
            resultado.append((inicio, fim))
        else:
            resultado[-1] = (resultado[-1][0], max(resultado[-1][1], fim))

    return resultado

#Resultado
intervalos = [(1, 4), (2, 5), (7, 9)]
print(mesclar_intervalos(intervalos)) 

