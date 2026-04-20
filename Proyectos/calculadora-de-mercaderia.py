"""
Sistema de Calculo de Precios
==============================
Ingresa un valor y el sistema calcula:

  1. Precio base     : valor ingresado - 10%
  2. Precio mayorista: precio base + 30%
  3. Precio unitario : (precio base x 1.60) / 12 unidades
"""

historial = []


def formatear(valor):
    return f"$ {valor:,.2f}"


def calcular_precios(ingresado):
    base      = ingresado * 0.90
    mayorista = base * 1.30
    unitario  = (base * 1.60) / 12
    return base, mayorista, unitario


def mostrar_resultado(ingresado, base, mayorista, unitario):
    ancho = 46
    print("\n" + "=" * ancho)
    print(f"  {'RESULTADO DE CALCULO':^{ancho - 4}}")
    print("=" * ancho)
    print(f"  Valor ingresado    : {formatear(ingresado)}")
    print(f"  Precio base        : {formatear(base)}  (-10%)")
    print(f"  Precio mayorista   : {formatear(mayorista)}  (base +30%)")
    print(f"  Precio unitario    : {formatear(unitario)}  (base x1.60 / 12 unidades)")
    print("=" * ancho)


def mostrar_historial():
    if not historial:
        print("\n  (El historial esta vacio.)")
        return
    ancho = 72
    print("\n" + "=" * ancho)
    print(f"  {'HISTORIAL DE CALCULOS':^{ancho - 4}}")
    print("=" * ancho)
    print(f"  {'#':<4} {'Ingresado':>12} {'Base (-10%)':>13} {'Mayorista':>13} {'Unitario (/12)':>15}")
    print("-" * ancho)
    for i, r in enumerate(historial, 1):
        print(
            f"  {i:<4}"
            f" {formatear(r['ingresado']):>12}"
            f" {formatear(r['base']):>13}"
            f" {formatear(r['mayorista']):>13}"
            f" {formatear(r['unitario']):>15}"
        )
    print("=" * ancho)


def menu():
    print("\n--- MENU ---")
    print("  1. Calcular nuevo precio")
    print("  2. Ver historial")
    print("  3. Limpiar historial")
    print("  4. Salir")
    return input("Elegi una opcion: ").strip()


def main():
    print("\n==========================================")
    print("     SISTEMA DE CALCULO DE PRECIOS        ")
    print("==========================================")

    while True:
        opcion = menu()

        if opcion == "1":
            entrada = input("\nIngresa el valor: $ ").strip()
            try:
                ingresado = float(entrada.replace(",", "."))
                if ingresado < 0:
                    print("  El valor no puede ser negativo.")
                    continue

                base, mayorista, unitario = calcular_precios(ingresado)
                mostrar_resultado(ingresado, base, mayorista, unitario)

                guardar = input("\nGuardar en historial? (s/n): ").strip().lower()
                if guardar == "s":
                    historial.append({
                        "ingresado": ingresado,
                        "base":      base,
                        "mayorista": mayorista,
                        "unitario":  unitario,
                    })
                    print("  Guardado correctamente.")

            except ValueError:
                print("  Valor invalido. Ingresa un numero.")

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            historial.clear()
            print("  Historial limpiado.")

        elif opcion == "4":
            print("\n  Hasta luego.\n")
            break

        else:
            print("  Opcion no valida. Elegi entre 1 y 4.")


if __name__ == "__main__":
    main()