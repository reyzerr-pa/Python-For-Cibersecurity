#¿Qué es una función?
#Una función es un bloque de código con nombre que podés ejecutar cuando quieras, las veces que quieras. En vez de repetir el mismo código, lo escribís una vez dentro de una función y lo llamás cuando lo necesitás.
#Analogía: pensá en una función como una receta. La escribís una vez y la podés usar cada vez que quieras cocinar ese plato, sin reescribirla."""

def nombre_de_la_funcion(parametros):
    #bloque de codigo
    return resultado


#def---> le dice a python que vas a definir una función
#nombre ---> el nombre que le das para llamarla despues 
#parametros ---> datos que le pasas (opcional)
#return --> el valor que devuelve (opcional)

"""Los 4 cocneptos que vamos aprender HOY """

# 1 Funcion Simple --> sin parametros ni return , solo ejecuta algo
# 2 Funcion con parametros --> recibe datos para trabajar pero no devuelve nada
# 3 Funcion con return --> devuelve un resultado pero no recibe datos
# 4 Funcion con parametros por defecto --> tiene valores predefinidos si no le pasas nada



"""
Ejercicio: Funciones en Python
================================
Descripción:
    Este ejercicio cubre los conceptos fundamentales de las funciones
    en Python: definición, parámetros, return y valores por defecto.

Autor: [Christian]
Fecha: Abril 2026
"""

# ─────────────────────────────────────────────
# CONCEPTO 1: Función simple (sin parámetros)
# ─────────────────────────────────────────────
# Una función simple agrupa código que queremos reutilizar.
# No recibe datos ni devuelve nada, solo ejecuta instrucciones.

def saludar():
    print("¡Hola! Bienvenido al ejercicio de funciones.")
    print("Hoy vas a aprender mucho.\n")

# Llamamos a la función escribiendo su nombre seguido de ()
saludar()
saludar()  # La podemos llamar cuantas veces queramos


# ─────────────────────────────────────────────
# CONCEPTO 2: Función con parámetros
# ─────────────────────────────────────────────
# Los parámetros son variables que le pasamos a la función
# para que trabaje con datos específicos.

def saludar_persona(nombre):
    # 'nombre' es un parámetro: recibe el valor que le pasemos
    print(f"¡Hola, {nombre}! Bienvenido.\n")

# Al llamar la función, le pasamos un argumento
saludar_persona("Ana")
saludar_persona("Carlos")


# ─────────────────────────────────────────────
# CONCEPTO 3: Función con return
# ─────────────────────────────────────────────
# 'return' hace que la función devuelva un resultado.
# Ese resultado lo podemos guardar en una variable o usar directamente.

def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado  # Devuelve el valor calculado

# Guardamos el resultado en una variable
total = sumar(5, 3)
print(f"5 + 3 = {total}")

# O lo usamos directamente
print(f"10 + 7 = {sumar(10, 7)}\n")


# ─────────────────────────────────────────────
# CONCEPTO 4: Parámetros por defecto
# ─────────────────────────────────────────────
# Podemos darle un valor por defecto a un parámetro.
# Si no se pasa ese argumento al llamar la función, usa el valor por defecto.

def presentar(nombre, edad, pais="Argentina"):
    # 'pais' tiene valor por defecto: si no se pasa, usa "Argentina"
    print(f"Nombre: {nombre}")
    print(f"Edad:   {edad}")
    print(f"País:   {pais}\n")

# Sin pasar 'pais' → usa "Argentina" por defecto
presentar("Lucas", 25)

# Pasando 'pais' → usa el valor que le damos
presentar("María", 30, "México")


# ─────────────────────────────────────────────
# EJERCICIO INTEGRADOR
# ─────────────────────────────────────────────
# Combinamos todo lo aprendido en una mini calculadora.

def calculadora(numero1, numero2, operacion="suma"):
    """
    Realiza una operación entre dos números.
    
    Parámetros:
        numero1  (float): Primer número
        numero2  (float): Segundo número
        operacion (str) : Operación a realizar (por defecto: 'suma')
    
    Retorna:
        float: El resultado de la operación
    """
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    elif operacion == "division":
        if numero2 == 0:
            print("⚠️  No se puede dividir por cero.")
            return None
        return numero1 / numero2
    else:
        print("⚠️  Operación no reconocida.")
        return None

# Probamos la calculadora
print("=== Mini Calculadora ===")
print(f"Suma:           {calculadora(10, 5)}")
print(f"Resta:          {calculadora(10, 5, 'resta')}")
print(f"Multiplicación: {calculadora(10, 5, 'multiplicacion')}")
print(f"División:       {calculadora(10, 5, 'division')}")
print(f"División x 0:   {calculadora(10, 0, 'division')}")