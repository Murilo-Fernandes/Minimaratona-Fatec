# Lê os valores dos dias
diaUm, diaDois, diaTres = map(int, input().split())

diffUmDois = diaDois - diaUm
diffDoisTres = diaTres - diaDois

# Verifica as condições e imprime os resultados
if diaUm > diaDois and diaDois <= diaTres:
    print(":)")
elif diaUm < diaDois and diaDois >= diaTres:
    print(":(")

if diaUm < diaDois and diaDois < diaTres:
    if diffDoisTres < diffUmDois:
        print(":(")
    else:
        print(":)")

if diaUm > diaDois and diaDois > diaTres:
    if diffDoisTres > diffUmDois:
        print(":)")
    else:
        print(":(")

if diaUm == diaDois:
    if diaDois < diaTres:
        print(":)")
    elif diaDois > diaTres:
        print(":(")
