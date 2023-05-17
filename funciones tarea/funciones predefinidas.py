import random

def sumarSeis(num = 3, num2 = 3):
    try:
        num = int(num)
        num2 = int(num2)
        if (num + num2 == 6):
            print ("{} + {} = 6".format(num,num2))
        else:
            print (f"{num} + {num2} : La suma de esos numeros no da 6")
    except ValueError:
        print("esos no son numeros")


def concatenarTexto(txt = "ejemplo para", txt2 = "concatenar", txt3 = "texto"):
    print ("{} {} {}".format(txt,txt2,txt3))


def nombreUsuario(txt = "Joe Doe"):
    if(type(txt)==str):
        print("Su nombre es {}".format(txt))
    else:
        print("Valor ingresado no es el correcto")


def sumar_restar_concatenar(num,num2,fun=0):
    match fun:
        case 1:
            print (num + num2)
        case 2:
            print (num - num2)
        case 3:
            print (str(num) + str(num2))


def realizar_encuesta(preguntas = ["cual es tu partido politico?","que opiinas del cambio climatico?"],usuario = "anonimo"):
    respuesta = []
    for i in preguntas:
        respuesta.append(input(i + ":    "))
        
    print("\n\n")

    for i in range(0,len(preguntas)):
        print (preguntas[i])
        print (str(usuario) + " respondio: " + str(respuesta[i]))