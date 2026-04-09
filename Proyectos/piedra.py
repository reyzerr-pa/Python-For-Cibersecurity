import random

minimo = 1
maximo = 10

numero_azar = random.randint(minimo, maximo)

while True:
    intento_usuario = int(input(" Introduce tu numero:  "  ))
    if numero_azar < intento_usuario :
        print ("Fallaste,  te as pasado "+ str (intento_usuario) )
    elif intento_usuario < numero_azar :
        print ("El numero es mas grande que " + str (intento_usuario))
    else:
        print("Ganaste")
        break
    