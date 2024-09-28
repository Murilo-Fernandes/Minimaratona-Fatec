quantidade_casos = int(input())

for _ in range(quantidade_casos):
    hora = int(input())
    minuto = int(input())
    ocorrencia = int(input())

    if ocorrencia == 1 and hora >= 24:
        hora_ajustada = 0
        print(f"{hora_ajustada}:{minuto:02d} - A porta abriu!")
    elif ocorrencia == 1 and hora < 24:
        print(f"{hora:02d}:{minuto:02d} - A porta abriu!")
    elif ocorrencia == 0 and hora >= 24:
        hora_ajustada = 0
        print(f"{hora_ajustada:02d}:{minuto:02d} - A porta fechou!")
    elif ocorrencia == 0 and hora < 24:
        print(f"{hora:02d}:{minuto:02d} - A porta fechou!")
