import json
import os

ARCHIVO_DATOS = "datos.json"

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


        