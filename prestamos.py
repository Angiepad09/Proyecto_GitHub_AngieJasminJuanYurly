def registrar_prestamo(inventario, prestamo):
    codigo = input("Ingrese el código del ítem: ").strip()
    usuario = input("Ingrese el nombre de usuario: ").strip()
    fecha = input("Ingrese la fecha del préstamo: ").strip()

    for item in inventario:
        if item["codigo"].lower() == codigo.lower():

            if item["cantidad_disponible"] <= 0:
                print("No hay unidades disponibles de este item")
                return

            item["cantidad_disponible"] -= 1

            nuevo_prestamo = {
                "codigo_item": item["codigo"],
                "usuario": usuario,
                "fecha": fecha,
                "devuelto": False
            }

            prestamo.append(nuevo_prestamo)

            print("Préstamo registrado correctamente")
            return

    print("No se encontró el item con ese código.")

def registrar_devolucion(inventario, prestamos):
    codigo = input("Ingrese el código del Item: ").strip()
    usuario = input("Ingrese su nombre de usuario: ").strip()

    for prestamo in prestamos:
        if (prestamo["codigo_item"].lower() == codigo.lower()
                and prestamo["usuario"].lower() == usuario.lower):

            if prestamo["devuelto"]:
                print("Este préstamo ya fue devuelto")
                return

            prestamo["devuelto"] = True

            for item in inventario:
                if item["codigo"].lower() == codigo.lower():
                    item["cantidad_disponible"] += 1
                    break

            print("Devolución registrada correctamente")
            return

    print("No se encontró un préstamo activo con estos datos.")