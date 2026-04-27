#Para crear un conjunto utilizo llave {} o la funcion set():


frutas = {"manzana", "banana", "naranja", "pera", "uva"}
numeros = set([1, 2, 3, 4, 5])

#Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), 
# la intersección (&), 
# la diferencia (-) y la diferencia simétrica (^).

#Union de Conjuntos 

numero1 = {1, 2, 3, 4, 5}
numero2 = {4, 5, 6, 7, 8}

union = numero1 | numero2
print(union)  # Imprime {1, 2, 3, 4, 5, 6, 7, 8}

#Intersección de Conjuntos (&)
interseccion = numero1 & numero2
#Que hace interseccion? Devuelve un nuevo conjunto que contiene solo los elementos que están presentes en ambos conjuntos.

print(interseccion)  # Imprime {4, 5}

#Diferencia de Conjuntos (-)
diferencia = numero1 - numero2  
#Que hace diferencia? Devuelve un nuevo conjunto que contiene los 
# elementos que están presentes en el primer conjunto pero no en el segundo.

print(diferencia)  # Imprime {1, 2, 3}

#Diferencia Simétrica de Conjuntos (^)
diferencia_simetrica = numero1 ^ numero2
#Que hace diferencia_simetrica? Devuelve un nuevo conjunto que contiene los elementos 
# que están presentes en uno de los conjuntos pero no en ambos. (los que se repiten no entran en el resultado)

print(diferencia_simetrica)  # Imprime {1, 2, 3, 6, 7, 8}

#Métodos de conjuntos
#Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#add(elemento): agrega un elemento al conjunto.
#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
#clear(): elimina todos los elementos del conjunto.

# Ejemplos de uso de métodos de conjuntos:

frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()