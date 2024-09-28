i = 0
qtdpares = 0
qtdimpares = 0
qtdpositivos = 0
qtdnegativos = 0

while i < 5:
    escolha = int(input(""))
    if escolha == 0:
        qtdpares += 1
    elif escolha % 2 == 0 and escolha > 0:
        qtdpositivos += 1
        qtdpares += 1
    elif escolha % 2 == 0 and escolha < 0:
        qtdnegativos += 1
        qtdpares += 1
    elif escolha % 2 != 0 and escolha > 0:
        qtdpositivos += 1
        qtdimpares += 1
    elif escolha % 2 != 0 and escolha < 0:
        qtdnegativos += 1
        qtdimpares += 1
    i += 1

print(f"{qtdpares} valor(es) pares")
print(f"{qtdimpares} valor(es) impares")
print(f"{qtdpositivos} valor(es) positivos")
print(f"{qtdnegativos} valor(es) negativos")
