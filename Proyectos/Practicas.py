numero = 7

if numero % 2 == 0:
    resultado = "El número es par."
else:
    resultado = "El número es impar."   
print(resultado)


def multiplicar(a, b):
    return a * b    
 
resultado = multiplicar (5, 3) + multiplicar (2, 4)
print(resultado)  # Imprime 15
#porque 5*3=15 y 2*4=8, entonces 15+8=23

#lo explico: la función multiplicar toma dos argumentos, a y b, y devuelve su producto. Luego,
#  se llama a la función multiplicar dos veces: primero con los argumentos 5 y 3, 
# lo que devuelve 15, y luego con los argumentos 2 y 4, lo que devuelve 8. Finalmente, 
# se suman los resultados de ambas llamadas a la función, dando como resultado final 23.