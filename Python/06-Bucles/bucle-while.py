# Descripcion:

# El bucle while ejecuta un bloque de codigo repetidamente minetras una condicion sea verdadera (TRUE) Es ideal cuando no sabemos de antemanno cauntas veces se repetira el bucle .
# Sintaxis:
# while condicion:
#     bloque de codigo


###### Ejemplo 1: Contar de 1 a 10 , usando una varible de control
import time

print("!!!!!!Preparados para la cuenta regresiva!!!!")
time.sleep(3)
contador = 5
while contador >= 0:
    print(contador)
    contador -= 1
    time.sleep(1)

print("Despegue!!! 🚀 Yaaaaaa")    

# Tanbien traje importa time para poder usar time.sleep() y hacer una pausa entre cada numero impreso, para que se vea mas realista la cuenta regresiva.
#agregando pausa en los anuncios tanbien para que se vea mas dramatico el despegue.


### Ejemplo 2:  Adivinar un numero secreto


num_secreto = False       
while not num_secreto:
    num_usuario = int(input("Adivina el numero secreto entre 1 y 10: "))
    if num_usuario == 7:
        print("Felicidades! Adivinaste el numero secreto! 🎉")
        num_secreto = True
    else:
        print("Intenta de nuevo! 😢")


### Ejemplo con while pero con aproximacion 

import time

num = 7
adivinando = False

while not adivinando:
    num_u = int(input("Inserta un numero entre 0 y 10 para adivinar el numero secreto: "))

    if num_u ==num:
        print("Felicidades! Adivinaste el numero secreto!  raro ...🎉")
        adivinando = True
    elif abs(num_u - num) <= 2:
        print("Estas muy cerca! Intenta de nuevo! 😢")