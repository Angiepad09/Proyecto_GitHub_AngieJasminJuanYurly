def registrar_prestamo(inventario, prestamo):
    codigo = input("Ingrese el código del ítem: ").strip()
    usuario = input("Ingrese el nombre de usuario: ").strip()
    fecha = input("Ingrese la fecha del prestamo: ").strip()

    for item in inventario:
        if item["codigo"].lower() == codigo.lower():

            if item["cantidad_disponible"] <= 0:
                print("No hay unidades disponibles de este item")
                return

            item["cantidad_disponible"] -= 1

            prestamo = {
                "codigo_item": item["codigo"],
                "usuario": usuario,
                "fecha": fecha,
                "devuelto": False
            }

            prestamos.append(prestamo)

            print("Prestamo registrado correctamente")
            return

        print("No se encontró el item con ese código.")