qtdocorrencias = 0
x = 0 
y = 0
i = 0 
qtdocorrencias = int(input(""))

while (i < qtdocorrencias):
    x = int(input(""))
    y = int(input(""))

    resultado = 0
    j = 0
    while (j < y):
        if (x % 2 != 0):
            resultado += x 
            x += 2
        elif (x % 2 == 0):
            x+=1
            resultado += x
            x+=2
        j+=1
    print(resultado)
    i+=1


    

