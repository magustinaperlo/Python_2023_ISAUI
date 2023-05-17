import random

def pi():
    print ("3.14")

def sumar45mas45():
    print (45 + 45)

def dinosaurioFavorito():

    dinosaurio = ["dilophosaurio", "indoraptor", "giganotosaurio","diabloceratops"]

    resultado = dinosaurio[random.randint(0,len( dinosaurio))]

    print (resultado)

def chistes():

    chiste1 = ["crimenes de guerra", "protestas", "derechos para la gente con enanismo","piedras en los riñones"]
    chiste2 = ["mi padre saliendo del closet", "la presidencia de Alberto Fernandes","una alta taza de mortalidad", "el colapso de las torres gemelas"]
    luck = random.randint(0,len(chiste1)-1)
    aa = chiste1[luck]
    luck = random.randint(0,len(chiste2)-1)
    bb = chiste2[luck]
    print ("no hay {}, sin {}".format(aa,bb))

def nolose():
    nolose = random.randint(0,1)
    if (nolose == 0):
        print("no lo se")
    if (nolose == 1):
        print("tampoco lo se")

#######################################################################################################################################

def miNombreEs(text):
    try:
        text = str(text)
        print ("mi nombre es:{}".format(text))

    except ValueError:
        text = "eso no es un nombre, mamahuevo"

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
        print ("text")

    except ValueError:
        print ("Debes ingresar un numero")

def ingresaTresNumerosParaLaLista(num, num2, num3):

    try:
        lista = [int(num), int(num2), int(num3)]
        print (lista)
    except ValueError:
        print ("Esos no son numeros")

def DibidirNumeros(num, num2):

    try:
        num = int(num)
        num2 = int(num2)
        print (num / num2)
    except ValueError:
        print("esos no son numeros")

###############################################################################################################################################

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

def concatenarTexto(txt = "viva", txt2 = "la", txt3 = "pachanga"):

    if ((type(txt)==str) and (type(txt2)==str) and (type(txt3)==str)):
        print ("{} {} {}".format(txt,txt2,txt3))

    else:
        print("Valor ingresado no es el correcto")

def nombreUsuario(txt = "Joe Doe"):

    if(type(txt)==str):
        print("Su nombre es {}".format(txt))
    else:
        print("Valor ingresado no es el correcto")

def crearListaComida(txt = "fideos",txt2 = "hamburguesa",txt3 = "helado"):
    listaComida = []
    if ((type(txt)==str) and (type(txt2)==str) and (type(txt3)==str)):

        return (listaComida[txt,txt2,txt3])
    else:
        print("Valor ingresado no es el correcto")

