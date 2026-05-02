#try
#EL bloque try se utiliza para envolver el código que puede generar una excepción. Si se produce una excepción dentro del bloque try, el programa no se detendrá, sino que se ejecutará el bloque except correspondiente.
#except     
#El bloque except se utiliza para manejar la excepción que se ha producido. Puedes especificar el tipo de excepción que deseas manejar o usar un bloque except genérico para manejar cualquier tipo de excepción.
#finally    
#El bloque finally se ejecuta siempre, independientemente de si se ha producido una excepción o no. Se utiliza para realizar tareas de limpieza, como cerrar archivos o liberar recursos.
#Ejemplo de manejo de excepciones en Python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes introducir un número válido.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
finally:
    print("Gracias por usar el programa.")  
#En este ejemplo, el bloque try intenta convertir la entrada del usuario a un número entero y luego realiza una división. Si el usuario introduce algo que no es un número, se generará una excepción ValueError, que será manejada por el primer bloque except. Si el usuario introduce cero, se generará una excepción ZeroDivisionError, que será manejada por el segundo bloque except. Cualquier otra excepción inesperada será manejada por el bloque except genérico. Finalmente, el bloque finally se ejecutará siempre, agradeciendo al usuario por usar el programa.


