
#print ((5 - 6.4)**2)

lista = [5,6,6,7,8]

equiz = []

con = 0
num = 0

for i in lista:

    num += i

    con += 1

prom = num / con

for i in lista:
    resta = ( i - prom )

    equiz.append(round(resta**2 , 10))

print (lista)

print (equiz)

suma = 0

for i in equiz:
    suma = suma + i 

print (suma / con)