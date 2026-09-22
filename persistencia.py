import json
import os

ARCHIVO_DATOS = "inventario.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return [], []

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return (
            datos.get("inventario", []),
            datos.get("prestamos", [])
        )

    except (json.JSONDecodeError, FileNotFoundError):
        return [], []
def guardar_datos(inventario, prestamos):
    datos = {
        "inventario": inventario,
        "prestamos": prestamos
    }

    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

        