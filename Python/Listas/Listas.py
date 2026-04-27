frutas = ["olano","banana", "naranja", "pera", "uva"]

#frutas.reverse()  # Invierte el orden de la lista
#print(frutas)  # Imprime la lista invertida

#frutas.sort()  # Ordena la lista alfabéticamente
#print(frutas)  # Imprime la lista ordenada ascedentemente

#fruta_elemento = frutas.pop(2) # Elimina y devuelve el elemento en la posición 2 (pera)
#print(fruta_elemento)  # Imprime "pera"

#frutas.remove("pera")  # Elimina "pera" de la lista
#remove es un metodo que se utiliza para eliminar un elemento de la lista, si el elemento no existe en la lista se genera un error

#frutas.append(elemento) es un metodo que se utiliza para agregar un elemento al final de la lista
#frutas.append("kiwi")  # Agrega "kiwi" al final de la lista


#.insert(posicion, elemento) es un metodo que se utiliza para insertar un elemento en una posicion especifica de la lista
#frutas.insert(0, "manzana")  # Agrega "manzana" en la posición 0 esta inserta al inicio de la lista

#print(frutas)  # Imprime la lista completa


#Inprimo todos los elementos de la lista usando su indice
"""print(frutas[0])  # Imprime el primer elemento (manzana)       
print(frutas[1])  # Imprime el segundo elemento (banana)
print(frutas[2])  # Imprime el tercer elemento (naranja)
print(frutas[3])  # Imprime el cuarto elemento (pera)
print(frutas[4])  # Imprime el quinto elemento (uva)

#Agregar los numeros negativamente 
print(frutas[-1])  # Imprime el último elemento (uva)
print(frutas[-2])  # Imprime el penúltimo elemento (pera)
print(frutas[-3])  # Imprime el antepenúltimo elemento (naranja)
print(frutas[-4])  # Imprime el cuarto elemento desde el final (banana)
print(frutas[-5])  # Imprime el quinto elemento desde el final (manzana)"""



#Listas de Compresion
#Es una forma concisa de crear listas a partir de iterables, aplicando una expresión a cada elemento y opcionalmente filtrando elementos con una condición.
#Ejemplo: Crear una lista de cuadrados de los números del 0 al 9        
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    

cuadrados = [x**2 for x in range(10)]

print(cuadrados)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]    



