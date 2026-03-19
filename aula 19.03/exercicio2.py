import math

hora = int(input("Hora (0–23): "))
chuva = int(input("Chuva (0 ou 1): "))
fluxo = int(input("Fluxo (0 baixo, 1 médio, 2 alto): "))

# Tempo base
if 7 <= hora <= 9 or 17 <= hora <= 19:
    tempo = 60
else:
    tempo = 35

# Ajustes
if chuva == 1:
    tempo *= 1.2

if fluxo == 2:
    tempo += 15
elif fluxo == 0:
    tempo -= 10

# Arredondar para cima
tempo_final = math.ceil(tempo)

print(f"Tempo final: {tempo_final} segundos")