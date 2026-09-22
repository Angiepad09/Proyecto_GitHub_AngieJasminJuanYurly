def registrar_prestamo(inventario, prestamo):
    codigo = input("Ingrese el código del ítem: ").strip()
    usuario = input("Ingrese el nombre de usuario: ").strip()
    fecha = input("Ingrese la fecha del prestamo: ").strip()

    for item in inventario:
        if item["codigo"].lower() == codigo.lower():

            if item["cantidad_disponible"] <= 0:
                print("No hay unidades disponibles de este item")
                return