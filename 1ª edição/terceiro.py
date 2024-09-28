quantidade_casos = int(input())

for _ in range(quantidade_casos):
    numero_um = int(input())
    letra = input().strip()
    numero_dois = int(input())

    if letra.isupper() and numero_um != numero_dois:
        print(numero_dois - numero_um)
    elif letra.islower() and numero_um != numero_dois:
        print(numero_dois + numero_um)
    elif numero_um == numero_dois:
        print(numero_um * numero_dois)
