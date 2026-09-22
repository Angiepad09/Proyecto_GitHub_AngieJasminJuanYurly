from persistencia import *
from inventario import *
from prestamos import *

inventario, prestamos = cargar_datos()

while True:

    try: 
        print("=" * 45)
        print("     BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE")
        print("=" * 45)
        print("1. Registrar ítem\n2. Listar ítems\n3. Buscar ítem\n4. Registrar préstamo\n5. Registrar devolución\n6. Salir")
        print("=" * 45)
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_item(inventario, prestamos)

        elif opcion == "2":
            listar_items(inventario)

        elif opcion == "3":
            buscar_item(inventario)

        elif opcion == "4":
           registrar_prestamo(inventario, prestamos)

        elif opcion == "5":
            registrar_devolucion(inventario, prestamos)

        elif opcion == "6":
            print("\nGracias por utilizar BiblioStock.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
    except ValueError:
        print("Ingrese una opcion del menu correcta")

    