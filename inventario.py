from persistencia import guardar_datos


def registrar_item(inventario, prestamos):
    print("\n========== REGISTRAR ÍTEM ==========")

    codigo = input("Ingrese el código del ítem: ").strip()

    for item in inventario:
        if item("codigo").lower() == codigo.lower():
            print("Error: ya existe un ítem con ese código.")
            return

    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad total: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                break

        except ValueError:
            print("Debe ingresar un número entero.")

    ubicacion = input("Ingrese la ubicación: ").strip()

    nuevo_item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "cantidad_total": cantidad,
        "cantidad_disponible": cantidad,
        "ubicacion": ubicacion
    }

    inventario.append(nuevo_item)

    guardar_datos(inventario, prestamos)

    print(f'\nÍtem "{titulo}" registrado exitosamente.')
    print(f"Disponibles: {cantidad}")


def listar_items(inventario):
    print("\n========== INVENTARIO ==========")

    if not inventario:
        print("No hay ítems registrados.")
        return

    for item in inventario:
        print("----------------------------------------")
        print(f"Código:              {item['codigo']}")
        print(f"Título:              {item['titulo']}")
        print(f"Autor:               {item['autor']}")
        print(f"Categoría:           {item['categoria']}")
        print(f"Cantidad total:      {item['cantidad_total']}")
        print(f"Cantidad disponible: {item['cantidad_disponible']}")
        print(f"Ubicación:           {item['ubicacion']}")

    print("----------------------------------------")


def buscar_item(inventario):
    print("\n========== BUSCAR ÍTEM ==========")

    busqueda = input("Ingrese el código o título: ").strip().lower()
    encontrados = []

    for item in inventario:
        if (busqueda in item["codigo"].lower() or busqueda in item["titulo"].lower()):
            encontrados.append(item)

    if not encontrados:
        print("No se encontraron ítems.")
        return

    for item in encontrados:
        print("----------------------------------------")
        print(f"Código:      {item['codigo']}")
        print(f"Título:      {item['titulo']}")
        print(f"Autor:       {item['autor']}")
        print(f"Categoría:   {item['categoria']}")
        print(f"Disponibles: {item['cantidad_disponible']}")
        print(f"Ubicación:   {item['ubicacion']}")

    print("----------------------------------------")