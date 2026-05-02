def suma(x, y, z):
    resultado = x + y + z
    print(resultado)

suma(1, 2, 3)
suma(4, 5, 6)
suma(7, 8, 9)
#LLamo 3 veces a la función suma, cada vez con diferentes números,
# y me imprime el resultado de la suma de esos números.


valores = input("Ingresa tres números separados por comas: ").split(",")
valores = [int(valor) for valor in valores]

def resta():
    resultado = valores[0] - valores[1] - valores[2]
    print(resultado)    

resta()
#Defino una lista de valores y 
# luego creo una función que resta esos valores.   


#Return es una palabra reservada que se utiliza para devolver 
# un valor desde una función.
#Cuando se ejecuta una función, el código dentro de la función 
# se ejecuta y luego

def multiplicacion(a, b):
    resultado = a * b
    return resultado

# Ejemplo de uso
print(multiplicacion(5, 3))  # Imprime 15

valorees = [4, 7, 2, 9]

def suma(valores):
    resultado = sum(valores)
    return resultado

print(suma(valorees))  # Imprime 22 