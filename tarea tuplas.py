import os

def tuplas_meses():
    tupla_meses = ( "" , "enero" , "febrero" ,"marzo", "abril", "mayo" , "junio" , "julio" , "agosto" , "septiembre" , "octubre" , "noviembre" , "diciembre" )

    while 1:

        num=int(input("ingrese un numero correspondiente a un mes:   "))

        if num == 0:
            os.system("cls")
            op = input("\nprograma terminado. Precione cualquier tecla para continuar:  ")
            break
        elif (num < 13) and (num > 0):
            for i in range(0,len(tupla_meses)):
                if i == num:
                    print (f"\n{tupla_meses[i]}\n")
        else:
            print ("\nvalor ingresado no es correcto\n")


######
######

def tupla_de_numeros():
    tupla_numeros = (1,1,4,4,4,2,3,3,3,3,5,5,6,7,7,7,7,8,8,9,9,9,9,9,10,11,12,12,12,12,12)

    while 1:
        con = 0
        try:
            num = int(input("Ingrese un numero mayor a 0 y menor a 13: "))
            if (num < 1) or (num > 12):
                print("numero fuera de tupla")
            else:
                print(f"El numero aparece {tupla_numeros.count(num)} vez en la tupla")
        except ValueError:
            print ("Lo que ingresaste no era un numero: ")


######
######

def tupla_mayor_menor():
    tupla_mayor = (23,67,32,34,56,78,90,120,101,44,89,13,66,99,34,41,57,71,22,79,104,134,20,21,119,118)
    mayor = tupla_mayor[0]
    menor = tupla_mayor[0]
    for i in tupla_mayor:
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i
    print(f"el numero menor de la tupla es {menor}, y el mayor es {mayor}")


######
######


def tupla_random():
    tupla_random = ("rana naranja","dinosaurio","el obelisco","mi padre en monopatin","russia","la virgen en aladelta","el quinto precidente de Bolivia","la final con Francia","una deuda millonaria","pollo a las brasas")

    while 1:
        num = int(input("Ingrese un indice para buscar oraciones random en una tupla:     "))

        if (num > -1) and (num < 10):
            print(tupla_random[num])
        else:
            print("valor ingresado fuera de rango")


######
######


def multiplos():

    bup = [1,2,3,4,5,6,7,8,9,10]

    for i in bup:
        con = 1
        msj = ""
        for k in range(0,10):
            msj = msj + f"{(con*i)}, "
            con += 1

        print (f"Tabla de {i} : " + msj)
