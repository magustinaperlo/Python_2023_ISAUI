import os

text = input("ingrese:  ")

lista = text.split()

con = 0

try:
    for i in lista:

        decim = False

        for k in i:
            
            if (k == ".") or (k == ","):
                decim = True
        
        if decim == True:
            lista[con] = float(i.replace("," , "."))
        else:
            lista[con] = int(i)

        con += 1

    aprobadp = True
except ValueError:
    print ("Debe ingresar una lista valida. Numeros enteros o decimales separados por espacios. Sin letras.\n")


print (lista)