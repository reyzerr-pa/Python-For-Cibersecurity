"""
#APRENDIENDO EL BUCLE FOR

for variable in elemento_iterable (lista, rango,etc)
En programación, el bucle for es fundamental para automatizar tareas 
repetitivas, como procesar filas de datos o leer archivos de configuración.
     Bloque de Instruciones


"""
contador = 0
resultado = 0

for contador in range (0, 10):
    print("Voy por el "+ str (contador))

    resultado += contador

print(f"El resultado es : {resultado}")


amigos = ["tamara", "raquel", "lopez"]

for amigo in amigos:
    print("hola " + amigo)


nombre = "Tamara"
apellido = "Lopez"