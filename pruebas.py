import random

largo = 9

ancho = 9

lista = []
text = ""
for i in range(0,largo):
    lista.append([0]*ancho)


for i in range(0,largo):
    text += "| "
    for k in range(0,ancho):
        lista[i][k] = random.randint(0,9)
        if ((k+1) < ancho):
            text += str(lista[i][k]) + " , "
        else:
             text += str(lista[i][k]) + " | "
    text += "\n"

print(text)