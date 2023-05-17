import random

def pi():
    print ("3.14")

def sumar45mas45():
    print (45 + 45)

def dinosaurioFavorito():

    dinosaurio = ["dilophosaurio", "indoraptor", "giganotosaurio","diabloceratops"]

    resultado = dinosaurio[random.randint(0,len( dinosaurio))]

    print (resultado)

def frases_motivacionales():

    chiste1 = ["felicidad", "10 horas de sueño diario", "un mejor futuro","razones para despertar cada dia"]
    chiste2 = ["peliculas de comedia", "un kilo de helado","tu amor", "el amor de tu vida"]
    luck = random.randint(0,3)
    aa = chiste1[luck]
    luck = random.randint(0,3)
    bb = chiste2[luck]
    print ("no hay {}, sin {}".format(aa,bb))

def dibujar_una_cara():
    print("""
   _____________
  /         __  |
 _|  ---   /  ' |
(_    @)   (  @ |
  |       _|     )
  |     ___     |
  |      _     /
  |    ________)
  |   |    /

    """)

#######################################################################################################################################

def repeat(max):
    con = 0
    while con < max:
        "repeat no existe en python. Usa for i"
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

dibujar_una_cara()