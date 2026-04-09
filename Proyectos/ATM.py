saldo = 100 
continuar = True

print("--- Bienvenido al Cajero ---")

while saldo > 0 and continuar:
    print(f"\nTu saldo actual es : ${saldo}")
    retirar = int(input("¿Cuanto dinero deseas retirar? ( 0 para salir ): "))
    
    
    if retirar == 0:
        continuar = False
        print("Saliendo del sistema...")
    elif retirar <= saldo:
        saldo = saldo - retirar
        print(f"Has retirado ${retirar}. ¡Recoge tu dinero!")
    else:
        print("Error: No tienes saldo suficiente para ese retiro.")

if saldo == 0:
    print("\nTe has quedado sin dinero. Tu cuenta está en 0.")

print("Gracias por usar nuestro cajero.")
