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
