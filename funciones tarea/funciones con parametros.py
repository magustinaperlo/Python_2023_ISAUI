import random

def repeat(max):
    con = 0
    while con < max:
        print ("repeat no existe en python. Usa for i")
        con+=1
        

def suma(num,num2):
    try:
        num = int(num)
        num2 = int(num2)
        print (num + num2)
    except ValueError:
        print("esos no son numeros")

def ingresarNumeroParaCitarTexto(num):

    try:
        num = int(num)
        match num:
            case 1:
                text = "Mira que te mando que te esfuerces y seas valiente; no temas ni desmayes, porque Jehová, tu Dios, estará contigo dondequiera que vayas."
            case 2:
                text = "¡Oh, memoria, enemiga mortal de mi descanso!”. “La virtud más es perseguida de los malos que amada de los buenos.” “La ingratitud es hija de la soberbia.” “La razón de la sinrazón que a mi razón se hace, de tal manera mi razón enflaquece, que con razón me quejo de la vuestra fermosura."
            case 3:
                text = "Simplemente tienes que poner un pie delante del otro y seguir adelante. Poner anteojeras y arar justo delante. A lo largo de toda nuestra vida el trabajo siempre estará presente, pues aunque poseamos grandes riquezas de una forma u otra siempre tendremos que trabajar."

            case _:
                text = "no tenemos tantas citas"
        print (text)

    except ValueError:
        print ("Debes ingresar un numero")

def crear_matriz_random(largo,ancho):
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


def DibidirNumeros(num, num2):

    try:
        num = int(num)
        num2 = int(num2)
        print (num / num2)
    except ValueError:
        print("esos no son numeros")